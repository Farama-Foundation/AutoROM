import ale_py
import os

def main():
    install_dir = ale_py.__file__
    install_dir = install_dir[:-11] + "ROM/"

    game_list = []
    freeze_list = []

    for f in freeze_list:
        print("Ignoring ",f)

    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    new_link_file = "link_map.txt"
    link_file_ref = open(os.path.join(__location__, new_link_file), "r")
    for l in link_file_ref:
        payload = l.split("^^^")
        game_name = install_dir + payload[0] + "/"+payload[0] + ".bin"
        if not payload[0] in freeze_list:
            game_list.append(game_name)

    ale = ale_py.ALEInterface()
    for g in game_list:
        ale.loadROM(g)

    print("Successfully passed smoke test")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        if sys.argv[1] == "-i":
            import AutoROM
            AutoROM.main(True)
    main()