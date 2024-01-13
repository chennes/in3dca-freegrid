# -*- coding: utf-8 -*-
# ***************************************************************************
# *                                                                         *
# * This program is free software: you can redistribute it and/or modify    *
# * it under the terms of the GNU General Public License as published by    *
# * the Free Software Foundation, either version 3 of the License, or       *
# * (at your option) any later version.                                     *
# *                                                                         *
# * This program is distributed in the hope that it will be useful,         *
# * but WITHOUT ANY WARRANTY; without even the implied warranty of          *
# * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the           *
# * GNU General Public License for more details.                            *
# *                                                                         *
# * You should have received a copy of the GNU General Public License       *
# * along with this program.  If not, see <http://www.gnu.org/licenses/>.   *
# *                                                                         *
# ***************************************************************************

import os
import FreeCAD as App
import FreeCADGui as Gui
from freecad.freegrid import ICONPATH

try:
    from FreeCADGui import Workbench
except ImportError as e:
    App.Console.PrintWarning(
        "you are using the FreeGridWorkbench with an old version of FreeCAD (<0.16)")
    App.Console.PrintWarning(
        "the class Workbench is loaded, although not imported: magic")

class FreeGridWorkbench(Gui.Workbench):
    """
    A FreeCAD Workbench that creates parametric storage solutions
    """

    MenuText = "FreeGrid"
    ToolTip = "FreeGrid 3D printed storage system"
    Icon = os.path.join(ICONPATH, "template_resource.svg")
    commands = ["CreateStorageBox", "CreateStorageGrid"]

    def Initialize(self):
        """
        This function is called at the first activation of the workbench.
        here is the place to import all the commands
        """

        # Add commmands to toolbar and menu

        from .FreeGridCmd import CreateStorageBox
        from .FreeGridCmd import CreateStorageGrid

        self.appendToolbar("FreeGrid", self.commands)
        self.appendMenu("FreeGrid", self.commands)

        Gui.addCommand('CreateStorageBox', CreateStorageBox())
        Gui.addCommand('CreateStorageGrid', CreateStorageGrid())

        App.Console.PrintMessage("FreeGrid Workbench initialized\n")

    def Activated(self):
        """
        Code which should be computed when a user switch to this workbench
        """
        App.Console.PrintMessage("\nHola\n")
        pass

    def Deactivated(self):
        """
        Code which should be computed when this workbench is deactivated
        """
        App.Console.PrintMessage("\nAdiós\n")
        pass

    def ContextMenu(self, recipient):
        """
        This is executed whenever the user right-clicks on screen
        "recipient" will be either "view" or "tree"
        """
        self.appendContextMenu(
            "FreeGrid", self.commands
        )  # add commands to the context menu

    def GetClassName(self):
        return "Gui::PythonWorkbench"

Gui.addWorkbench(FreeGridWorkbench())
