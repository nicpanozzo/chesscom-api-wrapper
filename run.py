from chesscomwrapper import ChesscomWrapper
nic = ChesscomWrapper().getPlayer("nicolapanozzo", lazy=True)
nic.profile
nic.profile

print(nic.profile.avatar)
