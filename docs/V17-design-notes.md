# Vive shoe V17 — September 24 PCB

Source snapshot: vive-pogo-source.step, copied from E:/Documents/GitHub/vive-pogo/vive-pogo.step (modified September 24, 2026, 22:56:51). The PCB repository was not edited.

Updated PCB is 21.5 x 10 x 0.8 mm, with 1 mm corner radii. The new resistor, copper and pads are included. Registration uses the connector's placement, preserving the corrected orientation toward the wrist strap and the existing 3-degree tilt.

The rear pocket's two closed corners now have 1.2 mm radii, adding a modest amount of plastic while retaining clearance around the 1 mm board corners. Front entrance corners stay open for insertion. The new corner operations are native editable Part cuts in the FreeCAD tree (V17 corner squares/arcs and rounded pocket tools). The pogo slot moved to match the new 2 mm pads at 3 mm spacing; it remains entirely in the rear shell.

Both shells clear the seated board, connector, copper and added resistor in the model. The PCB screw geometry is checked against the new assembly. Hardware remains four McMaster 96817A840 M2 x 4 screws per shoe. Nominal floor remains 0.60 mm.

Sampled insertion check: twelve positions with the PCBA 0.4 mm below final seating height clear the shell. Smallest sampled clearance is approximately 0.014 mm. This is a tight prototype fit, not a continuous path proof or allowance for all manufacturing tolerances. Physically test insertion and screw-head protrusion before finalizing the dock.

Only the rear shell requires reprinting. Front shell geometry is unchanged. Use RearShell-UPRIGHT.step for printing, or the corresponding STL. These enclosure checks do not constitute electrical or PCB fabrication approval.
