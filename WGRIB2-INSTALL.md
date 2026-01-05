# SailWatchPro: wgrib2 Install Guide

**Maintainer Note:**  
This document describes the step-by-step process to install the wgrib2 executable on a Mac.
wgrib2 provides functionality for interacting with, reading, writing, and manipulating grib2 files

---

## Setup Steps

```$	brew install miniforge```

```$	conda init zsh```

<p>Close and repoen a new terminal shell</P>

```$	conda create -n grib python=3.11```

```$	conda activate grib```

```$	conda install -c conda-forge wgrib2```

```$	wgrib2 -version```

_Short link: [this file is WGRIB2-INSTALL.md in your repo root]_

---
