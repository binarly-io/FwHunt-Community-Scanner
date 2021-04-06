# uefi_r2: tools for analyzing UEFI firmware using radare2
#
# SPDX-License-Identifier: GPL-3.0+
#
# pylint: disable=missing-module-docstring

EFI_BOOT_SERVICES_X64 = {
    0x00000018: "RaiseTPL",
    0x00000020: "RestoreTPL",
    0x00000028: "AllocatePages",
    0x00000030: "FreePages",
    0x00000038: "GetMemoryMap",
    0x00000040: "AllocatePool",
    0x00000048: "FreePool",
    0x00000050: "CreateEvent",
    0x00000058: "SetTimer",
    0x00000060: "WaitForEvent",
    0x00000068: "SignalEvent",
    0x00000070: "CloseEvent",
    0x00000078: "CheckEvent",
    0x00000080: "InstallProtocolInterface",
    0x00000088: "ReinstallProtocolInterface",
    0x00000090: "UninstallProtocolInterface",
    0x00000098: "HandleProtocol",
    0x000000A0: "Reserved",
    0x000000A8: "RegisterProtocolNotify",
    0x000000B0: "LocateHandle",
    0x000000B8: "LocateDevicePath",
    0x000000C0: "InstallConfigurationTable",
    0x000000C8: "LoadImage",
    0x000000D0: "StartImage",
    0x000000D8: "Exit",
    0x000000E0: "UnloadImage",
    0x000000E8: "ExitBootServices",
    0x000000F0: "GetNextMonotonicCount",
    0x000000F8: "Stall",
    0x00000100: "SetWatchdogTimer",
    0x00000108: "ConnectController",
    0x00000110: "DisconnectController",
    0x00000118: "OpenProtocol",
    0x00000120: "CloseProtocol",
    0x00000128: "OpenProtocolInformation",
    0x00000130: "ProtocolsPerHandle",
    0x00000138: "LocateHandleBuffer",
    0x00000140: "LocateProtocol",
    0x00000148: "InstallMultipleProtocolInterfaces",
    0x00000150: "UninstallMultipleProtocolInterfaces",
    0x00000158: "CalculateCrc32",
    0x00000160: "CopyMem",
    0x00000168: "SetMem",
    0x00000170: "CreateEventEx",
}

EFI_RUNTIME_SERVICES_X64 = {
    0x00000018: "GetTime",
    0x00000020: "SetTime",
    0x00000028: "GetWakeupTime",
    0x00000030: "SetWakeupTime",
    0x00000038: "SetVirtualAddressMap",
    0x00000040: "ConvertPointer",
    0x00000048: "GetVariable",
    0x00000050: "GetNextVariableName",
    0x00000058: "SetVariable",
    0x00000060: "GetNextHighMonotonicCount",
    0x00000068: "ResetSystem",
    0x00000070: "UpdateCapsule",
    0x00000078: "QueryCapsuleCapabilities",
    0x00000080: "QueryVariableInfo",
}

EFI_SMM_SYSTEM_TABLE2_X64 = {
    0x00000028: "SmmInstallConfigurationTable",
    0x00000030: "SmmIo",
    0x00000050: "SmmAllocatePool",
    0x00000058: "SmmFreePool",
    0x00000060: "SmmAllocatePages",
    0x00000068: "SmmFreePages",
    0x00000070: "SmmStartupThisAp",
    0x00000078: "CurrentlyExecutingCpu",
    0x00000080: "NumberOfCpus",
    0x00000088: "CpuSaveStateSize",
    0x00000090: "CpuSaveState",
    0x00000098: "NumberOfTableEntries",
    0x000000A0: "SmmConfigurationTable",
    0x000000A8: "SmmInstallProtocolInterface",
    0x000000B0: "SmmUninstallProtocolInterface",
    0x000000B8: "SmmHandleProtocol",
    0x000000C0: "SmmRegisterProtocolNotify",
    0x000000C8: "SmmLocateHandle",
    0x000000D0: "SmmLocateProtocol",
    0x000000D8: "SmiManage",
    0x000000E0: "SmiHandlerRegister",
    0x000000E8: "SmiHandlerUnRegister",
}

BS_PROTOCOLS = [
    "InstallProtocolInterface",
    "ReinstallProtocolInterface",
    "UninstallProtocolInterface",
    "HandleProtocol",
    "RegisterProtocolNotify",
    "OpenProtocol",
    "CloseProtocol",
    "OpenProtocolInformation",
    "ProtocolsPerHandle",
    "LocateHandleBuffer",
    "LocateProtocol",
    "InstallMultipleProtocolInterfaces",
    "UninstallMultipleProtocolInterfaces",
]

BS_PROTOCOLS_INFO_X64 = {
    "InstallProtocolInterface": {"offset": 0x80, "reg": "rdx"},
    "ReinstallProtocolInterface": {"offset": 0x88, "reg": "rdx"},
    "UninstallProtocolInterface": {"offset": 0x90, "reg": "rdx"},
    "HandleProtocol": {"offset": 0x98, "reg": "rdx"},
    "RegisterProtocolNotify": {"offset": 0xA8, "reg": "rcx"},
    "OpenProtocol": {"offset": 0x118, "reg": "rdx"},
    "CloseProtocol": {"offset": 0x120, "reg": "rdx"},
    "OpenProtocolInformation": {"offset": 0x128, "reg": "rdx"},
    "ProtocolsPerHandle": {"offset": 0x130, "reg": "rdx"},
    "LocateHandleBuffer": {"offset": 0x138, "reg": "rdx"},
    "LocateProtocol": {"offset": 0x140, "reg": "rcx"},
    "InstallMultipleProtocolInterfaces": {"offset": 0x148, "reg": "rdx"},
    "UninstallMultipleProtocolInterfaces": {"offset": 0x150, "reg": "rdx"},
}

OFFSET_TO_SERVICE = dict(
    [(BS_PROTOCOLS_INFO_X64[s]["offset"], s) for s in BS_PROTOCOLS_INFO_X64]
)
