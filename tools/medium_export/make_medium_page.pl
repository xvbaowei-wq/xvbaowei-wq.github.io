# Transform the canonical English article into a Medium-import helper page:
# - display math -> downloaded equation PNGs (block images)
# - inline math  -> downloaded equation PNGs (inline images)
# - Hugo math-display wrappers removed
# Usage: perl tools/medium_export/make_medium_page.pl
use strict;
use warnings;
use URI::Escape;

my $src = "content/plasma-physics/magnetic-mirror-reflection-force/index.en.md";
my $outdir = "content/medium-import/mm-v3";
my $eqdir = "$outdir/eq";
mkdir "content/medium-import" unless -d "content/medium-import";
mkdir $outdir unless -d $outdir;
mkdir $eqdir unless -d $eqdir;

open my $fh, "<:raw", $src or die $!;
local $/;
my $t = <$fh>;
close $fh;
$t =~ s/\r//g;

# strip front matter
$t =~ s/\A---\n.*?\n---\n//s;

my @jobs;   # (formula, display?, filename)
my $nd = 0;
my $ni = 0;

sub sanitize {
    my ($f) = @_;
    $f =~ s/\\thinspace\{\}/\\,/g;
    $f =~ s/\s*\n\s*/ /g;
    return $f;
}

# headings: replace math with Unicode text and emit raw HTML
# (PaperMod markdown headings get anchor "#" links that Medium imports as text)
sub heading_unicode {
    my ($h) = @_;
    $h =~ s/\$\\nabla\\cdot\\mathbf B=0\$/∇·B=0/g;
    $h =~ s/\$B_r\$/Bᵣ/g;
    $h =~ s/\$\\theta\+d\\theta\$/θ+dθ/g;
    $h =~ s/\$\\theta\$/θ/g;
    $h =~ s/\$r\+dr\$/r+dr/g;
    $h =~ s/\$z\+dz\$/z+dz/g;
    $h =~ s/\$r\$/r/g;
    $h =~ s/\$z\$/z/g;
    return $h;
}
$t =~ s{^### (.+)$}{ "<h3>" . heading_unicode($1) . "</h3>" }gme;
$t =~ s{^## (.+)$}{ "<h2>" . heading_unicode($1) . "</h2>" }gme;

# captions: keep math as Unicode text (Medium turns inline images into blocks,
# which would split captions mid-sentence)
for my $line (split /\n/, $t) {
    if ($line =~ /^\*Figure \d/ && $line =~ /\$/) {
        my $orig = $line;
        $line =~ s/\$d\\theta\$/dθ/g;
        $line =~ s/\$\\theta\$/θ/g;
        $line =~ s/\$dr\$/dr/g;
        $line =~ s/\$dz\$/dz/g;
        $line =~ s/\$z\$/z/g;
        $t =~ s/\Q$orig\E/$line/;
    }
}

# display blocks wrapped in math-display divs
$t =~ s{<div class="math-display">\n\$\$\n(.*?)\n\$\$\n</div>}{
    my $f = sanitize($1);
    $nd++;
    my $fn = sprintf("eq/display-%03d.png", $nd);
    push @jobs, [$f, 1, $fn];
    "\n![equation]($fn)\n";
}gse;

# any remaining bare $$ blocks (should not happen)
$t =~ s{\$\$\n?(.*?)\n?\$\$}{
    my $f = sanitize($1);
    $nd++;
    my $fn = sprintf("eq/display-%03d.png", $nd);
    push @jobs, [$f, 1, $fn];
    "\n![equation]($fn)\n";
}gse;

# inline math
$t =~ s{\$([^\$\n]+?)\$}{
    my $f = sanitize($1);
    $ni++;
    my $fn = sprintf("eq/inline-%03d.png", $ni);
    push @jobs, [$f, 0, $fn];
    "![]($fn)";
}gse;

# copy figure files referenced
for my $img ($t =~ /!\[[^\]]*\]\((fig-[^)]+)\)/g) {
    system("cp", "content/plasma-physics/magnetic-mirror-reflection-force/$img", "$outdir/$img") == 0
        or die "copy $img failed";
}

my $fm = <<'EOF';
---
title: "From ∇·B = 0 to the Magnetic Mirror Force: A Complete Near-Axis Derivation"
date: 2026-09-17T08:44:00+08:00
draft: false
description: "A complete near-axis derivation of the magnetic mirror force, starting from ∇·B = 0 in cylindrical coordinates."
math: false
showToc: false
robotsNoIndex: true
sitemap:
  exclude: true
_build:
  list: never
---
EOF

open my $of, ">:raw", "$outdir/index.md" or die $!;
print $of $fm, "\n", $t;
close $of;

# write download manifest: filename<TAB>url
open my $mf, ">:raw", "$outdir/jobs.tsv" or die $!;
for my $j (@jobs) {
    my ($f, $disp, $fn) = @$j;
    my $dpi = $disp ? 200 : 200;
    my $url = "https://latex.codecogs.com/png.image?%5Cdpi%7B$dpi%7D%5Cbg%7Bwhite%7D" . uri_escape($f);
    print $mf "$fn\t$url\n";
}
close $mf;
print "display: $nd, inline: $ni\n";
