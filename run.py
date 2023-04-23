from chesscomwrapper import ChessWrapper
nic = ChessWrapper().getPlayer("nicolapanozzo", lazy=True)
nic.profile
nic.profile

print(nic.profile.avatar)
