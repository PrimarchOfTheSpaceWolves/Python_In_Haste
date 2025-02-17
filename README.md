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
Miniconda is a smaller version of Anaconda, which is a distribution of Python.  It allows you to create environments.  One advantage of this is, should something get completely kerfuffled with the packages, you can always destroy the environment and start over.

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

***For Windows:*** Open "Anaconda Prompt (miniconda3)" **as an administrator**.  

***For Linux:*** If conda is installed system-wide, make sure the commands that follow are run using ``sudo``.

Create your environment (I will name this one HASTE):
```
conda create -n HASTE python=3.11
```

Before installing any packages to the new environment, activate it:
```
conda activate HASTE
```

```(HASTE)``` should now be to the left of your terminal prompt.

## Installing Packages

***For Windows:*** Open "Anaconda Prompt (miniconda3)" **as an administrator**.  

***For Linux:*** If conda is installed system-wide, make sure the commands that follow are run using ``sudo``.

Activate your environment:
```
conda activate HASTE
```

### Updating pip
With your environment activated, make sure pip is updated:

```
python -m pip install --upgrade pip
```

### Installing PyTorch
With ```HASTE``` activated, you will need to install PyTorch for deep learning.  

The latest instructions for installing PyTorch may be found [here](https://pytorch.org/get-started/locally/).

#### CUDA-Enabled PyTorch
If you have an NVIDIA graphics card (or intend to run this environment on a machine with one), you will want to install the CUDA-enabled version of PyTorch.

The following instructions are for **CUDA version 12.6**.

##### Windows

```
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu126
```

##### Linux

```
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu126
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

### Installing Other Python Packages

I recommend you also install the following packages:
```
pip3 install tensorboard
pip3 install pandas
pip3 install scikit-learn scikit-image 
pip3 install matplotlib 
pip3 install pytest
pip3 install opencv-python
conda install conda-pack
```

### Python Environment Troubleshooting

* If you need to remove the environment:
```
conda remove --name HASTE --all
```

* If you encounter path issues (where conda isn't found once you activate an environment), open an Anaconda prompt as admin and try the following to add conda to your path globally: 
```
conda init
```

## Visual Code
I strongly recommend Visual Code as your IDE.
* [Download](https://code.visualstudio.com/) and install Visual Code
  * I suggest enabling the context menu options.
  * ***For Mac:*** Follow [these instructions](https://code.visualstudio.com/docs/setup/mac)
* Install the following extensions:  
  * **"Python Extension Pack"** by Don Jayamanne  
  * **"Git Graph"** by mhutchie
  * **"Markdown All in One"** by Yu Zhang

A terminal can always be created/opened with ```View menu -> Terminal```.  However, if you need to restart, click the garbage can icon on the terminal window to destroy it.

***For Windows:*** Change your default terminal from Powershell to Command Prompt:
1. ```View menu -> Command Palette -> "Terminal: Select Default Profile"```
2. Choose ```"Command Prompt"```
3. Close any existing terminals in Visual Code

Once you open a project, to make sure you are using the correct Python interpreter:
1. Close any open terminals with the garbage can icon
2. Open a .py file
3. ```View -> Command Palette -> "Python: Select interpreter"```
4. Choose the one located at under the ```HASTE``` environment.
5. If the GPU is not being utilized (or you see errors about paths to CUDA libraries not being found), type the following in your terminal to manually activate your environment: ```HASTE\Scripts\activate.bat``` (you will need whatever path is before ```HASTE```)
   
