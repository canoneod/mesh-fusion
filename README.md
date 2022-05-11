# Watertight and Simplified Meshes through TSDF Fusion

This repository contains a simply Python pipeline for obtaining watertight
and simplified meshes from arbitrary triangular meshes, given in `.off` format.
The approach is largely based on adapted versions of Gernot Riegler's
[pyrender](https://github.com/griegler/pyrender) and [pyfusion](https://github.com/griegler/pyfusion);
it also uses [PyMCubes](https://github.com/pmneila/PyMCubes).

If you use any of this code, please make sure to cite the following work:

    @article{Stutz2018ARXIV,
        author    = {David Stutz and Andreas Geiger},
        title     = {Learning 3D Shape Completion under Weak Supervision},
        journal   = {CoRR},
        volume    = {abs/1805.07290},
        year      = {2018},
        url       = {http://arxiv.org/abs/1805.07290},
    }

See the GitHub repositories above for additional citations.
Also check the corresponding [project page](http://davidstutz.de/projects/shape-completion/).

## Several modification to fit my need
- Current for CUDA 11.6 compatiblity and other dependencies, added in environment.yml
- In libfusiongpu/ CMakelists.txt was modifed to fit my gpu(1050ti) compute compatiblity(mine supported 6.1)
- modified __init__.py of libfusiongpu/ and librender/ & copied *.so files of each to root folder and renamed them.
- simplification.mlx was changed to fit to pymeshlab
- for other troubles and usages, check out original repository

Copyright (c) 2018 David Stutz, Max-Planck-Gesellschaft

**Please read carefully the following terms and conditions and any accompanying documentation before you download and/or use this software and associated documentation files (the "Software").**

The authors hereby grant you a non-exclusive, non-transferable, free of charge right to copy, modify, merge, publish, distribute, and sublicense the Software for the sole purpose of performing non-commercial scientific research, non-commercial education, or non-commercial artistic projects.

Any other use, in particular any use for commercial purposes, is prohibited. This includes, without limitation, incorporation in a commercial product, use in a commercial service, or production of other artefacts for commercial purposes.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

You understand and agree that the authors are under no obligation to provide either maintenance services, update services, notices of latent defects, or corrections of defects with regard to the Software. The authors nevertheless reserve the right to update, modify, or discontinue the Software at any time.

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software. You agree to cite the corresponding papers (see above) in documents and papers that report on research using the Software.
