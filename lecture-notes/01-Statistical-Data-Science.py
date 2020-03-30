# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.3.4
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown] slideshow={"slide_type": "slide"}
# # PSTAT 234 - Statistical Data Science <a class="tocSkip">
#     
#
# ## Sang-Yun Oh <a class="tocSkip">

# %% [markdown] slideshow={"slide_type": "slide"}
# # What is Data Science?

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## (Classical) Scientific Method
#
# * Scientific method used since ~1200s and formalized in 1500s
#
# * Roughly, scientific method is an approach [[reference](https://en.wikipedia.org/wiki/Scientific_method)]
#
#     * Question
#     * Hypothesis
#     * Prediction
#     * Testing
#     * Analysis
#
# * No one clear definition [[reference](https://plato.stanford.edu/entries/scientific-method/)]

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## New Paradigm of Science
#
# **Fourth Paradigm: Data-intensive scientific discovery** (Jim Gray): everything about science is changing

# %% [markdown] slideshow={"slide_type": "fragment"}
# * Scope of Research has broadened: **Basic science vs. Business insight**

# %% [markdown] slideshow={"slide_type": "fragment"}
# * "Some models are useful": **Precise vs. Approximate**

# %% [markdown] slideshow={"slide_type": "fragment"}
# * What is more important? **Understanding vs. Prediction**

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Data Science is ...
#
# * A multi-disciplinary field that uses scientific methods, processes, algorithms and systems to extract knowledge and insights from structured and unstructured data [reference](https://doi.org/10.1145/2500499)
#
# * Merger of statistics, data analysis, machine learning and their related methods in order to understand and analyze actual phenomena with data [reference](https://doi.org/10.1007/978-4-431-65950-1_3)
#
# * Composed of techniques and theories drawn from many fields within the context of mathematics, statistics, computer science, and information science. [reference](https://www.microsoft.com/en-us/research/publication/fourth-paradigm-data-intensive-scientific-discovery/)

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Beginnings of Data Science
#
# ![Cleveland](images/data-science-cleveland.png)
# [[International Statistical Review](http://doi.org/10.2307/1403527)]

# %% [markdown] slideshow={"slide_type": "subslide"}
# The article proposed data science program to train a new generation of data analysts:
#
# * **Domain expertise**: data analysis collaborations in subject matter areas.
#
# * **Mathematics/Statistics**: models, estimation, and distribution based on probabilistic inference.
#
# * **Computing**: hardware and software; computational algorithms
#     
# * **Theory**: foundations of data science; mathematical investigations of models and methods
#     
#
# [International Statistical Review](http://doi.org/10.2307/1403527)

# %% [markdown] slideshow={"slide_type": "subslide"}
#

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Data Scientific Approach
#
# ![DataScienceLifeCycle](images/DataScienceLifeCycle.jpg)
# [[UC Berkeley, School of Information](https://datascience.berkeley.edu/about/what-is-data-science/)]

# %% [markdown] slideshow={"slide_type": "slide"}
# # Computational Environment

# %% [markdown] slideshow={"slide_type": "subslide"}
# <table style="width: 100%;">
#     <tr>
#     <td style="width: 50%;"> <img src="images/jupyternotebook.png" alt="Drawing" style="width: 100%;"/> </td>
#     <td style="width: 50%;"> <img src="images/jupyterlab.png" alt="Drawing" style="width: 100%;"/> </td>
#     </tr>
#     <tr>
#     <td style="text-align: center; font-weight: bold;"/> Jupyter Notebook <br> (default) </td>
#     <td style="text-align: center; font-weight: bold;"/> Jupyter Lab <br> (optional) </td>
#     </tr>
# </table>

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Jupyter Notebooks vs. Jupyter Lab
#
# - Jupyter cluster is here: https://pstat134.lsit.ucsb.edu
#
# - If your username is `[UCSB NetID]`,  
#
# - Jupyter Notebook (default): `https://pstat134.lsit.ucsb.edu/user/[UCSB NetID]/tree`  
#
# - Jupyter Lab (optional): `https://pstat134.lsit.ucsb.edu/user/[UCSB NetID]/lab`   

# %% [markdown] slideshow={"slide_type": "fragment"}
# - **Jupyter Notebook + Additional Features = Jupyter Lab**

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Jupyter Notebook
#
# - Notebook environment: code, formatted text, and graphics
#
# - Conversion to other formats: e.g. markdown, latx, PDF, HTML, etc.
#
# - Interactivity HTML widgets
#
# ![Jupyter Notebook](images/jupyternotebook.png)

# %% [markdown] slideshow={"slide_type": "subslide"}
# - "Kernels" accessible through Jupyter include Python, shell, R, Julia, others  
#     [Jupyter kernels](https://github.com/jupyter/jupyter/wiki/Jupyter-kernels)  
#     ![Jupyter Diagram](images/jupyter-diagram.jpg)
#

# %% [markdown] slideshow={"slide_type": "fragment"}
# - Read [Jupyter notebook basics](https://github.com/jupyter/notebook/blob/master/docs/source/examples/Notebook/Notebook%20Basics.ipynb)

# %% [markdown] slideshow={"slide_type": "subslide"}
# ### Writing formatted text
#
# - Text formatting with [markdown syntax](https://guides.github.com/features/mastering-markdown/)

# %% [markdown] slideshow={"slide_type": "fragment"}
# - Math equations with latex commands:  
#     e.g., `$$ \hat \mu = \frac{1}{n}\sum_{i=1}^n x_i $$` produces:
#     $$ \hat \mu = \frac{1}{n}\sum_{i=1}^n x_i,\qquad \hat\sigma^2 = \frac{1}{n}\sum_{i=1}^n (x_i-\hat\mu)^2 $$
#     [Mathpix](https://mathpix.com/)

# %% [markdown] slideshow={"slide_type": "fragment"}
# - Images with `![Not Lazy](http://thoughtfulcampaigner.org/wp-content/uploads/2017/10/im-not-lazy-im-just-in-energy-saving-mode-sleepy-cat.jpg)`

# %% [markdown] slideshow={"slide_type": "fragment"}
# ![Not Lazy](http://thoughtfulcampaigner.org/wp-content/uploads/2017/10/im-not-lazy-im-just-in-energy-saving-mode-sleepy-cat.jpg)

# %% [markdown] slideshow={"slide_type": "fragment"}
# - Markdown is everywhere: e.g., [Github Flavored Markdown (GFM)](https://guides.github.com/features/mastering-markdown/#GitHub-flavored-markdown)

# %% [markdown] slideshow={"slide_type": "subslide"}
# ### More than Python
#
# - Python interpreter
#
# - IPython is short for interactive Python with additional functionality  
#     e.g., tab completion, syntax highlighting, magic, etc. (Chapter 1 in Vanderplas)  
#
# - IPython's "[line, cell] magic" commands  
#     e.g., debugging, code timing, shell commands, execute external script, etc.

# %% [markdown] slideshow={"slide_type": "subslide"}
# ### Line magic: `%`
#
# - [Demo] Debugging example: `%debug`, etc.
#
# - [`xmode`](https://jakevdp.github.io/PythonDataScienceHandbook/01.06-errors-and-debugging.html#Controlling-Exceptions:-%xmode): Exception handler mode
#
# - More detail on debugging: [Vanderplas - Chapter 1](https://jakevdp.github.io/PythonDataScienceHandbook/01.06-errors-and-debugging.html)

# %% [markdown] slideshow={"slide_type": "slide"}
# #### Example: Debugging

# %% hideCode=false hideOutput=false slideshow={"slide_type": "-"}
# exception mode to verbose output
# %xmode Plain
# # %xmode Verbose

from IPython.core.debugger import set_trace

def func1(a, b):
    return a / b

def func2(x):
    
    a = x
    #set_trace()
    b = x - 1
    return func1(a, b)

# Refer to https://docs.python.org/3/library/pdb.html#debugger-commands
# Press h for help
# Uncomment below to trigger an error
# func2(1) 


# %% slideshow={"slide_type": "slide"}
# After an exception occurs, calling %debug 
# starts the debugger at last error
# uncomment the next line for demo
# # %debug

# input following at ipdb prompt
# print(a)
# print(b)

# %% [markdown] slideshow={"slide_type": "slide"}
# #### Other magic commands
#
# - [many more](https://www.datacamp.com/community/tutorials/tutorial-jupyter-notebook)

# %% slideshow={"slide_type": "-"}
# shift-tab for documentation
# %lsmagic

# %% [markdown] slideshow={"slide_type": "subslide"}
# ### Cell magic: `%%`
#
# - Entire cell is interpreted differently
#
# #### Example: Measuring running time

# %% slideshow={"slide_type": "-"}
# %%timeit -n500 -r10
total = []
for i in range(1000):
    total += [i]

# %% slideshow={"slide_type": "fragment"}
# %%timeit -n500 -r10
total = [i for i in range(1000)]

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Command-Line Interface (Bash Shell)
#
# ---
#
# * [Bash](https://en.wikipedia.org/wiki/Bash_(Unix_shell)): text (command-line) interface to operating system (OS)
#
# * OS (e.g. Windows, MacOS) handles file operations, interfacing with network, etc 
#
# * Run system operations using text commands
#
#     ```bash
#     echo "######## hello" > somefile.txt ## prints string into file 'somefile.txt'
#     ls -alh                              ## list files in directory
#     cat somefile.txt                     ## print contents of 'somefile.txt'
#     rm somefile.txt                      ## remove 'somefile.txt'
#     ``` 

# %% [markdown] slideshow={"slide_type": "subslide"}
# * [Explain Shell](https://explainshell.com/)
#
# * **Demo**: Use `git` command to clone a repository from Github  
#     _Note: self-learning git is recommended but not required for the course_ [[Software carpentry lesson: git](https://swcarpentry.github.io/git-novice/)]
#     
# * More on command line later    

# %% [markdown] slideshow={"slide_type": "subslide"}
# ### Example: Run bash commands: `%%bash`
#
# Bash is a shell scripting language. Bash language can coexist in Jupyter notebook. 

# %% slideshow={"slide_type": "fragment"} language="bash"
#
# echo "######## hello" > somefile.txt
# cat somefile.txt
# echo "######## did you see a hello?"
# echo "######## listing files"
# rm somefile.txt
# ls -alh

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Example: Jupyter Notebook and Bash
#
# - [Who is Jovyan?](https://github.com/jupyter/docker-stacks/issues/358)
# - ["In science fiction, a Jovian is an inhabitant of the planet Jupiter."](https://en.wikipedia.org/wiki/Jovian_%28fiction%29)
#
# Shell output can be saved into a Python variable

# %% slideshow={"slide_type": "fragment"}
nbfiles = !ls *.ipynb  # store filenames in nbfiles variable

for f,one in enumerate(nbfiles):
    print("file", f, ":", one)

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Example: Exporting notebooks
#
# - Notebooks can be converted using [`nbconvert`](https://nbconvert.readthedocs.io/en/latest/)
#     - Slides
#     - Static web pages  
#         e.g. auto-updating reporting, blogs, etc
#
# - Shell script to automated execution  
#     `jupyter nbconvert --to html --execute mynotebook.ipynb`
