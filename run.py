from chesscomwrapper import ChessWrapper
nic = ChessWrapper().getPlayer("nicolapanozzo")
nic.getProfile()

print(nic.profile.name)
