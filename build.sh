#!/bin/bash

# Compile the CV
docker run --rm -v $(pwd):/workdir texlive/texlive:latest xelatex /workdir/cv.tex

