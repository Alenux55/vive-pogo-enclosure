"""Export the saved shell geometry; run with FreeCAD's Python environment."""
from pathlib import Path
import FreeCAD as App
import MeshPart

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'cad' / 'Vive-Shoe.FCStd'

def main():
    doc = App.openDocument(str(SOURCE))
    try:
        for name in ('FrontShell', 'RearShell'):
            shape = doc.getObject(name + 'Export').Shape.copy()
            if not shape.isValid() or len(shape.Solids) != 1:
                raise ValueError(name + ': expected one valid solid')
            shape.exportStep(str(ROOT / 'exports' / 'assembly' / (name + '.step')))
            shape.translate(App.Vector(0, 0, -shape.BoundBox.ZMin))
            target = ROOT / 'exports' / 'print' / (name + '-UPRIGHT')
            shape.exportStep(str(target.with_suffix('.step')))
            mesh = MeshPart.meshFromShape(Shape=shape, LinearDeflection=0.025,
                                         AngularDeflection=0.1, Relative=False)
            if not mesh.isSolid():
                raise ValueError(name + ': mesh is not closed')
            mesh.write(str(target.with_suffix('.stl')))
            print('Exported ' + name)
    finally:
        App.closeDocument(doc.Name)

if __name__ == '__main__':
    main()
