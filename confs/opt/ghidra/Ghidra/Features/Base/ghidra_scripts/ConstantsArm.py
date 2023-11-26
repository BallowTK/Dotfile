# Replace Linux/ARM numeric constants with human readable names.
# @author b0bb
# @category Pwn
# @keybinding
# @menupath Analysis.Pwn.Constants.arm.arm
# @toolbar

import ghidra.app.util.opinion.ElfLoader as ElfLoader
from lib.Constants import Constants


def run():
    if currentProgram.getExecutableFormat() != ElfLoader.ELF_NAME:
        popup("Not an ELF file, cannot continue")
        return

    arch = "arm"
    abi = "default"

    Constants(currentProgram, currentSelection, monitor, state, arch, abi)


run()
