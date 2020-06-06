import multi_agent_ale_py
import os

def main():
    install_dir = multi_agent_ale_py.__file__
    install_dir = install_dir[:-11] + "ROM/"

    game_list = []


    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    new_link_file = "link_map.txt"
    link_file_ref = open(os.path.join(__location__, new_link_file), "r")
    for l in link_file_ref:
        payload = l.split("^^^")
        game_name = install_dir + payload[0] + "/"+payload[0] + ".bin"
        game_list.append(game_name)

    ale = multi_agent_ale_py.ALEInterface()
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