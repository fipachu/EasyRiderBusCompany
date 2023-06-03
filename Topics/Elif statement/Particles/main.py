spin, charge = input(), input()

if spin == "1/2":
    print("Strange Quark" if charge == "-1/3"
          else "Charm Quark" if charge == "2/3"
          else "Electron Lepton" if charge == "-1"
          else "Neutrino Lepton" if charge == "0"
          else "There is no particle with provided characteristics.")
else:
    print("Photon Boson" if charge == "0"
          else "There is no particle with provided characteristics.")
