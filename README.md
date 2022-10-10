# python-occ-demos

Wanted to try out methods for generating 3D CAD drawings parametrically (i.e. programatically). 

There seem to be quite a few libraries to do this and I know very little about CAD.  I tested 2 or 3 here with mixed results.


## pythonocc-core

This library was mentioned in [this stackoverflow post](https://stackoverflow.com/q/14519057/1609514) in 2013.

I installed it from here:
 - https://anaconda.org/conda-forge/pythonocc-core

It was a bit of a pain. Had to install a few other bits and bobs (e.g. Qt5) and then it still didn't work.  Had to uninstall and reinstall and then it worked.

The only documentation I could find is here and it's quite limited (parts are out of date):
 - https://pythonocc-doc.readthedocs.io/en/latest/

However there are lots of example scripts and notebooks which seem to be up to date.

I wanted to try out the exporting of models to files. [STEP](https://en.wikipedia.org/wiki/ISO_10303-21)(.stp), [X3D](.x3d) and [STL](https://en.wikipedia.org/wiki/STL_(file_format)) (.stl) seem to work, but STEP seems to be the most widely used.

However, I didn't find Python-OCC very user-friendly.

## CadQuery

Source code is here: https://github.com/CadQuery/cadquery
Documentation is here: https://cadquery.readthedocs.io/en/latest/

Had one installation issue which was promptly fixed by installing with conda instead of pip, thanks to a [response from the developers](https://github.com/CadQuery/cadquery/issues/1174).

I found this quite easy to use.  It is a heavily object-oriented programming library with quite high level, useful functionality such as splines and sweeps which is what I was looking for.  It also has an editor so you can view your construction.  In fact the python script is embedded in the editor (not run from the console on your machine), so you could say it is an IDE (integrated development environment).  It also exports drawing files to STEP.


## PyMesh

I also tried out [PyMesh](https://pymesh.readthedocs.io/en/latest/) but I'm not that experienced with Docker so it took me a while to get it working.  It seems to be more low-level than CADQuery and focussed on processing very complex meshes.  Might be more useful for 3D printing or making 3D game objects than CAD drawings for regular manufacturing.


## Open3D

Seems to be a numerical tool for automatically generating a 3D mesh out of a point cloud.  See this article in Towards Data Science:
- [5-Step Guide to generate 3D meshes from point clouds with Python](https://towardsdatascience.com/5-step-guide-to-generate-3d-meshes-from-point-clouds-with-python-36bad397d8ba).

## FreeCAD

I downloaded and successfully installed [FreeCAD](https://www.freecadweb.org). This is a complete, open source CAD design application which happens to utilise Python for automating many operations as well as parametric modelling and design.  Quite impressive, all-round CAD software application.

Documentation is here and looks comprehensive:
 - https://wiki.freecadweb.org/Main_Page

Here is a page introducing the Python scripting capabilities:
 - https://wiki.freecad.org/Python_scripting_tutorial
 
