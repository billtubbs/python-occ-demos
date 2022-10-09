# Simple demo of the Python CadQuery library for building
# parametric 3D CAD models.
#
# Instructions
# ------------
#
# Install CadQuery and CQ-Editor as described here:
#  - https://cadquery.readthedocs.io
#
# Launch the CQ-Editor and run this script from the editor
# by pressing the 'render' button.
#
# Uses the spline function to create two closed 2D 
# shapes with curved edges and the sweep function
# to create a solid by sweeping longitudinally from
# the first shape to the second.

import os
import cadquery as cq

results_dir = 'results'
if not os.path.exists(results_dir):
    os.mkdir(results_dir)

# Path to sweep along
path = cq.Workplane("XZ").lineTo(10, 0)
result = (
    cq.Workplane("YZ")
    .workplane(offset=0.0)
    .lineTo(2.0, 0)  # 1st 2D shape
    .spline(
        [(0, 1)], 
        tangents=[(0, 2), (-0.1, 0)],
        scale=False,
        includeCurrent=True
    )
    .close()
    .workplane(offset=10.0)
    .lineTo(1.6, 0)  # 2nd 2D shape
    .spline(
        [(0, 0.8)], 
        tangents=[(0, 2), (-0.1, 0)],
        scale=False,
        includeCurrent=True
    )
    .close()
    .sweep(path, multisection=True)
)

# Render the solid
show_object(result)

# Export as STEP file for further processing
filename = 'sweep_spline.step'
cq.exporters.export(result, os.path.join(results_dir, filename))
