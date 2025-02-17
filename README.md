# Python In Haste
***Author: Dr. Michael J. Reale***
***SUNY Polytechnic Institute***

You want to learn Python in a great hurry.  I assume you have worked with some other kind of language that is similar (C, C++, Java, R, MATLAB).

## Software Setup Overview
While you can install any distribution of Python you like and use any IDE you like, I recommend:
- Miniconda Python
- Visual Code

Once Miniconda is installed, you will have to create a miniconda environment.

## Miniconda Installation
Miniconda is a smaller version of Anaconda, which is a distribution of Python.

### Windows

First, download the latest installer for Windows [here](https://docs.conda.io/projects/miniconda/en/latest/).

Run the installer; I would install it for All Users (especially if your username has spaces in it).  I installed it into ```C:/miniconda3```.

Open "Anaconda Prompt (miniconda3)" **as an administrator**; you should see ```(base)``` to the left of your terminal prompt.

### Linux

First, download the latest version:
```
mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm -rf ~/miniconda3/miniconda.sh
```

Next, install it into your home directory (default options are fine):
```
~/miniconda3/bin/conda init bash
```

Close and reopen the terminal; you should see ```(base)``` to the left of your terminal prompt.

### Mac
Open up a terminal.

If you are on an **Intel Mac**:
```
curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh
sh Miniconda3-latest-MacOSX-x86_64.sh
```
If you are on an **M1 Mac**:
```
curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.sh
sh Miniconda3-latest-MacOSX-arm64.sh
```
Close and reopen the terminal; you should see ```(base)``` to the left of your terminal prompt.

## Python Environment Creation

Create your DATA3D environment:
```
conda create -n DATA3D python=3.11
```

Before installing any packages to the new environment, activate it:
```
conda activate DATA3D
```

```(DATA3D)``` should now be to the left of your terminal prompt.

## Installing Packages

***For Windows:*** Open "Anaconda Prompt (miniconda3)" **as an administrator**.  

***For Linux:*** If conda is installed system-wide, make sure the commands that follow are run using ``sudo``.

Activate your environment:
```
conda activate DATA3D
```

### Updating pip
On Linux in particular, with your environment activated, make sure pip is updated:

```
python -m pip install --upgrade pip
```

### Installing PyTorch
With ```DATA3D``` activated, you will need to install PyTorch for deep learning.  

The latest instructions for installing PyTorch may be found [here](https://pytorch.org/get-started/locally/).

#### CUDA-Enabled PyTorch
If you have an NVIDIA graphics card (or intend to run this environment on a machine with one), you will want to install the CUDA-enabled version of PyTorch.

***NOTE:*** On Linux, a version of Open3D may be installed that is pytorch-enabled, allowing usage of Open3D-ML.  However, accordingly to the documentation, you must install ```torch==2.2.2+cu121``` and ```torchvision==0.17.2+cu121```.  For consistency, we will use these versions for Windows and Mac as well.

The following instructions are for **CUDA version 12.1**.

##### Windows

```
pip3 install torch==2.2.2+cu121 torchvision==0.17.2+cu121 torchaudio --index-url https://download.pytorch.org/whl/cu121
```

##### Linux

```
pip3 install torch==2.2.2+cu121 torchvision==0.17.2+cu121 torchaudio --index-url https://download.pytorch.org/whl/cu121
```

#### CPU/Mac PyTorch
If you do NOT have an NVIDIA card (and/or are on a Mac), you will need to settle for the default installation:

```
pip3 install torch torchvision torchaudio
```

### Verifying PyTorch
To verify Pytorch works correctly:
```
python -c "import torch; x = torch.rand(5, 3); print(x); print(torch.cuda.is_available())"
```
You should see an array printed.  

If you have an NVIDIA card and installed the CUDA version of PyTorch, you should also see the word ```True``` (otherwise, ```False``` is expected).

### Installing Open3D
To install Open3D:
```
pip3 install open3d
```
This should also install Open3D-ML.

### Verifying Open3D
To verify Open3D has been installed correctly:
```
python -c "import open3d as o3d; print(o3d.__version__)"

python -c "import open3d as o3d; mesh = o3d.geometry.TriangleMesh.create_sphere(); mesh.compute_vertex_normals(); o3d.visualization.draw(mesh, raw_mode=True)"
```
First, the version of Open3D installed should print out.  Then, you should see a visualization window pop up.

To verify the command-line applications work:
```
open3d example visualization/draw
```
Similarly, a series of visualization windows should pop up.

### Verifying Open3D-ML
To verify Open3D-ML has been installed correctly:
```
pip3 install tensorboard
python -c "import open3d.ml.torch as ml3d"
```
***Under Linux***, this line should execute without errors.

### Installing Other Python Packages

Then, run the following commands to install the necessary packages for this course:
```
pip3 install tensorboard
pip3 install py3dtiles
pip3 install deepgeo
pip3 install pandas
pip3 install scikit-learn scikit-image 
pip3 install matplotlib 
pip3 install pytest
conda install conda-pack
```

### Python Environment Troubleshooting

* If you need to remove the DATA3D environment (the LOCAL version, not the portable one):
```
conda remove --name DATA3D --all
```

* If you encounter path issues (where conda isn't found once you activate an environment), open an Anaconda prompt as admin and try the following to add conda to your path globally: 
```
conda init
```


