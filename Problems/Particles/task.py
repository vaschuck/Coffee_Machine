spin = input()
charge = input()


if spin == '1':
    print('Photon Boson')
elif charge == '0':
    print('Muon Lepton')
elif charge == '-1':
    print('Electron Lepton')
elif charge == '2/3':
    print('Charm Quark')
else:
    print('Strange Quark')
