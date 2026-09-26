# Vive shoe — September 24 PCB

Source snapshot: vive-pogo-source.step, copied from E:/Documents/GitHub/vive-pogo/vive-pogo.step (modified September 24, 2026, 22:56:51). The PCB repository was not edited.

Updated PCB is 21.5 x 10 x 0.8 mm, with 1 mm corner radii. The new resistor, copper and pads are included. Registration uses the connector's placement, preserving the corrected orientation toward the wrist strap and the existing 3-degree tilt.

The rear pocket's two closed corners now have 1.2 mm radii, adding a modest amount of plastic while retaining clearance around the 1 mm board corners. Front entrance corners stay open for insertion. The new corner operations are native editable Part cuts in the FreeCAD tree (corner squares/arcs and rounded pocket tools). The pogo slot moved to match the new 2 mm pads at 3 mm spacing; it remains entirely in the rear shell.

Both shells clear the seated board, connector, copper and added resistor in the model. The PCB screw geometry is checked against the new assembly. Hardware remains four McMaster 96817A840 M2 x 4 screws per shoe. Nominal floor remains 0.60 mm.

Sampled insertion check: twelve positions with the PCBA 0.4 mm below final seating height clear the shell. Smallest sampled clearance is approximately 0.014 mm. This is a tight prototype fit, not a continuous path proof or allowance for all manufacturing tolerances. Physically test insertion and screw-head protrusion before finalizing the dock.

September 25 printability update: both shells now have editable 0.8 mm fillets on the exposed outer upper rim. The inner controller-contact rim, shell mating plane and bed-contact edge remain unchanged. The front shell's horizontal screw-head recesses now have native sketch-and-extrusion 45-degree roofs, reducing non-bed downward-facing area above 45 degrees by approximately 39.2 percent. Their circular lower clearance is retained. The rear shell also has a native 1.0 mm chamfer around the connector-side edges of the PCB-cavity ceiling. This reduced the rear STL's downward-facing area above 45 degrees from approximately 483.5 to 452.9 mm2; excluding the bed-contact underside, the reduction is approximately 20.6 percent. The flat PCB boss and seating faces remain unchanged so their functional datums are preserved.

Both shells therefore require reprinting to evaluate the complete update. Use the corresponding `FrontShell-UPRIGHT` and `RearShell-UPRIGHT` STEP files. When Bambu Support for PLA/PETG is available, use it for interface layers only and keep ordinary model filament for the support base. These enclosure checks do not constitute electrical or PCB fabrication approval.
