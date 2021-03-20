import tkinter as tk
import requests
import json
import math

# triggers = json.loads(json.dumps('[{"trigger": "sys_gametime","name": "Played the game", "points": 1},{"trigger": "we_mainquestcomplete", "name": "Main Quest", "points": 50},{"trigger": "we_shrinequestcomplete", "name": "Shrine Quest", "points": 30},{"trigger": "we_sidequestcomplete", "name": "Side Quest", "points": 50},{"trigger": "we_registerhorse","name": "Register a Horse", "points": 20},{"trigger": "we_weaponexpand","name": "Weapon Slot Expansion", "points": 15},{"trigger": "we_towerget","name": "Activate a Sheikah Tower", "points": 100},{"trigger": "we_armorupgrade","name": "Armor Upgrade", "points": 15},{"trigger": "we_trackedenemy", "name": "Defeated major enemy", "points": 50},{"trigger": "mi_korok","name": "Korok Seed", "points": 20},{"trigger": "mi_spiritorb","name": "Spirit Orb", "points": 50},{"trigger": "mi_paraglider","name": "Paraglider", "points": 50},{"trigger": "mi_heartcontainer","name": "Heart Container", "points": 50},{"trigger": "mi_staminavessel","name": "Stamina Vessel", "points": 50},{"trigger": "mi_sensorplus","name": "Sensor+","points": 50},{"trigger": "mi_stasisplus","name": "Stasis+","points": 50},{"trigger": "mi_bombplus","name": "Bomb+","points": 50},{"trigger": "tc_goldrupee","name": "Gold Rupee", "points": 20},{"trigger": "tc_silverrupee","name": "Silver Rupee", "points": 10},{"trigger": "tc_purplerupee","name": "Purple Rupee", "points": 7},{"trigger": "tc_giantcore","name": "Giant Ancient Core", "points": 15},{"trigger": "tc_ancientcore","name": "Ancient Core", "points": 7},{"trigger": "i_diamond", "name": "Diamond", "points": 30},{"trigger": "i_ruby", "name": "Ruby", "points": 15},{"trigger": "i_topaz", "name": "Topaz", "points": 12},{"trigger": "i_sapphire","name": "Sapphire", "points": 20},{"trigger": "i_opal","name": "Opal", "points": 7},{"trigger": "i_amber","name": "Amber", "points": 5},{"trigger": "i_ancientarrow","name": "Ancient Arrow", "points": 10},{"trigger": "i_icearrow", "name": "Ice Arrow", "points": 5},{"trigger": "i_firearrow", "name": "Fire Arrow", "points": 5},{"trigger": "i_shockarrow", "name": "Shock Arrow", "points": 5},{"trigger": "i_bombarrow", "name": "Bomb Arrow", "points": 5},{"trigger": "i_food","name": "Food", "points": 3},{"trigger": "i_pot","name": "Elixers", "points": 3},{"trigger": "i_new","name": "Some new item", "points": 2},{"trigger": "mi_hylianshield","name": "Hylian Shield", "points": 100},{"trigger": "mi_miphasgrace","name": "Mipha\'s Grace", "points": 200},{"trigger": "mi_entermipha", "name": "Enter Vah Ruta", "points": 100},{"trigger": "mi_revalisgale","name": "Revali\'s Gale", "points": 200},{"trigger": "mi_enterrevalis", "name": "Enter Vah Medoh", "points": 100},{"trigger": "mi_daruksprotection", "name": "Daruk\'s Protection", "points": 200},{"trigger": "mi_enterdaruk", "name": "Enter Vah Rudania", "points": 100},{"trigger": "mi_urbosasfury", "name": "Urbosa\'s Fury", "points": 200},{"trigger": "mi_enterurbosa","name": "Enter Vah Naboris", "points": 100},{"trigger": "mi_mastersword","name": "Master Sword", "points": 250},{"trigger": "we_beatgame","name": "Beat the Game", "points": 500},{"trigger": "mi_championmiphaboss", "name": "Champion\'s Ballad - Mipha Boss", "points": 200},{"trigger": "mi_championmiphashrine", "name": "Champion\'s Ballad - Mipha Shrine", "points": 50},{"trigger": "mi_championrevaliboss", "name": "Champion\'s Ballad - Revali Boss", "points": 200},{"trigger": "mi_championrevalishrine", "name": "Champion\'s Ballad - Revali Shrine", "points": 50},{"trigger": "mi_championdarukboss", "name": "Champion\'s Ballad - Daruk Boss", "points": 200},{"trigger": "mi_championdarukshrine", "name": "Champion\'s Ballad - Daruk Shrine", "points": 50},{"trigger": "mi_championurbosaboss", "name": "Champion\'s Ballad - Urbosa Boss", "points": 200},{"trigger": "mi_championurbosashrine", "name": "Champion\'s Ballad - Urbosa Shrine", "points": 50},{"trigger": "mi_shrineresurrection", "name": "Champion\'s Ballad - Shrine of Resurrection", "points": 250},{"trigger": "mi_memory","name": "Memory", "points": 50},{"trigger": "mi_trialofthesword", "name": "Trials of the Sword", "points": 250},]'))
triggers = json.loads('[{"trigger": "sys_gametime","name": "Played the game", "points": 1},{"trigger": "we_mainquestcomplete", "name": "Main Quest", "points": 50},{"trigger": "we_shrinequestcomplete", "name": "Shrine Quest", "points": 30},{"trigger": "we_sidequestcomplete", "name": "Side Quest", "points": 50},{"trigger": "we_registerhorse","name": "Register a Horse", "points": 20},{"trigger": "we_weaponexpand","name": "Weapon Slot Expansion", "points": 15},{"trigger": "we_towerget","name": "Activate a Sheikah Tower", "points": 100},{"trigger": "we_armorupgrade","name": "Armor Upgrade", "points": 15},{"trigger": "we_trackedenemy", "name": "Defeated major enemy", "points": 50},{"trigger": "mi_korok","name": "Korok Seed", "points": 20},{"trigger": "mi_spiritorb","name": "Spirit Orb", "points": 50},{"trigger": "mi_paraglider","name": "Paraglider", "points": 50},{"trigger": "mi_heartcontainer","name": "Heart Container", "points": 50},{"trigger": "mi_staminavessel","name": "Stamina Vessel", "points": 50},{"trigger": "mi_sensorplus","name": "Sensor+","points": 50},{"trigger": "mi_stasisplus","name": "Stasis+","points": 50},{"trigger": "mi_bombplus","name": "Bomb+","points": 50},{"trigger": "tc_goldrupee","name": "Gold Rupee", "points": 20},{"trigger": "tc_silverrupee","name": "Silver Rupee", "points": 10},{"trigger": "tc_purplerupee","name": "Purple Rupee", "points": 7},{"trigger": "tc_giantcore","name": "Giant Ancient Core", "points": 15},{"trigger": "tc_ancientcore","name": "Ancient Core", "points": 7},{"trigger": "i_diamond", "name": "Diamond", "points": 30},{"trigger": "i_ruby", "name": "Ruby", "points": 15},{"trigger": "i_topaz", "name": "Topaz", "points": 12},{"trigger": "i_sapphire","name": "Sapphire", "points": 20},{"trigger": "i_opal","name": "Opal", "points": 7},{"trigger": "i_amber","name": "Amber", "points": 5},{"trigger": "i_ancientarrow","name": "Ancient Arrow", "points": 10},{"trigger": "i_icearrow", "name": "Ice Arrow", "points": 5},{"trigger": "i_firearrow", "name": "Fire Arrow", "points": 5},{"trigger": "i_shockarrow", "name": "Shock Arrow", "points": 5},{"trigger": "i_bombarrow", "name": "Bomb Arrow", "points": 5},{"trigger": "i_food","name": "Food", "points": 3},{"trigger": "i_pot","name": "Elixers", "points": 3},{"trigger": "i_new","name": "Some new item", "points": 2},{"trigger": "mi_hylianshield","name": "Hylian Shield", "points": 100},{"trigger": "mi_miphasgrace","name": "Mipha\'s Grace", "points": 200},{"trigger": "mi_entermipha", "name": "Enter Vah Ruta", "points": 100},{"trigger": "mi_revalisgale","name": "Revali\'s Gale", "points": 200},{"trigger": "mi_enterrevalis", "name": "Enter Vah Medoh", "points": 100},{"trigger": "mi_daruksprotection", "name": "Daruk\'s Protection", "points": 200},{"trigger": "mi_enterdaruk", "name": "Enter Vah Rudania", "points": 100},{"trigger": "mi_urbosasfury", "name": "Urbosa\'s Fury", "points": 200},{"trigger": "mi_enterurbosa","name": "Enter Vah Naboris", "points": 100},{"trigger": "mi_mastersword","name": "Master Sword", "points": 250},{"trigger": "we_beatgame","name": "Beat the Game", "points": 500},{"trigger": "mi_championmiphaboss", "name": "Champion\'s Ballad - Mipha Boss", "points": 200},{"trigger": "mi_championmiphashrine", "name": "Champion\'s Ballad - Mipha Shrine", "points": 50},{"trigger": "mi_championrevaliboss", "name": "Champion\'s Ballad - Revali Boss", "points": 200},{"trigger": "mi_championrevalishrine", "name": "Champion\'s Ballad - Revali Shrine", "points": 50},{"trigger": "mi_championdarukboss", "name": "Champion\'s Ballad - Daruk Boss", "points": 200},{"trigger": "mi_championdarukshrine", "name": "Champion\'s Ballad - Daruk Shrine", "points": 50},{"trigger": "mi_championurbosaboss", "name": "Champion\'s Ballad - Urbosa Boss", "points": 200},{"trigger": "mi_championurbosashrine", "name": "Champion\'s Ballad - Urbosa Shrine", "points": 50},{"trigger": "mi_shrineresurrection", "name": "Champion\'s Ballad - Shrine of Resurrection", "points": 250},{"trigger": "mi_memory","name": "Memory", "points": 50},{"trigger": "mi_trialofthesword", "name": "Trials of the Sword", "points": 250}]')
global curUid, curScore, curTrigger, curPoints
curUid = ""
curScore = 0
curTrigger = ""
curPoints = 0

MAX_COL = 3


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.user_frame = None
        self.trigger_frame = None
        self.submit_frame = None
        self.create_widgets(1)

    def create_widgets(self, todo):

        row = 0
        col = 0

        if todo==1:
            self.user_frame = tk.Frame(self.master)
            self.user_frame.pack()
            self.info = json.loads(requests.get("http://71.206.247.211:3000/leaderboard").text)

            for i in self.info:
                if not "dummy" in i and not i == "":
                    req = json.loads(requests.get("https://g9b1fyald3.execute-api.eu-west-1.amazonaws.com/master/users/"+str(i.split("|")[0])).text)['result']['username']
                    self.i = tk.Button(self.user_frame)
                    self.i["text"] = req
                    self.i["command"] = lambda arg1=i.split("|")[0] , arg2=i.split("|")[1] : self.set_user(arg1, arg2)
                    # self.i["command"] = self.set_user(i.split("|")[0] , i.split("|")[1])
                    self.i.grid(row=row, column=col)
                    col+=1
                    if col%MAX_COL==0:
                        row+=1
                        col=0
            self.quit = tk.Button(self.user_frame, text="QUIT", fg="red",
                                  command=self.master.destroy)
            self.quit.grid(row=row+1, column=math.floor(MAX_COL/2)+1)
            self.reset = tk.Button(self.user_frame, text="RESET", fg="purple",
                                  command=self.reset_frame)
            self.reset.grid(row=row+1, column=math.floor(MAX_COL/2)-1)
        elif todo==2:
            self.trigger_frame = tk.Frame(self.master)
            self.trigger_frame.pack()
            for z in triggers:
                self.z = tk.Button(self.trigger_frame)
                self.z["text"] = z['name']
                self.z["command"] = lambda arg1=z['trigger'] , arg2=z['points']  : self.set_trigger(arg1, arg2)
                self.z.grid(row=row, column=col)
                col+=1
                if col%MAX_COL==0:
                    row+=1
                    col=0
            self.quit = tk.Button(self.trigger_frame, text="QUIT", fg="red",
                                  command=self.master.destroy)
            self.quit.grid(row=row+1, column=math.floor(MAX_COL/2)+1)
            self.reset = tk.Button(self.trigger_frame, text="RESET", fg="purple",
                                  command=self.reset_frame)
            self.reset.grid(row=row+1, column=math.floor(MAX_COL/2)-1)
        elif todo==3:
            self.submit_frame = tk.Frame(self.master)
            self.submit_frame.pack()
            total = curPoints+curScore
            message = '{"player": "'+curUid+'","triggerid": "'+curTrigger+'", "points": '+str(curPoints)+', "totalpoints": '+str(total)+'}'
            self.submit = tk.Text(self.submit_frame, wrap=tk.WORD, height=1, width=len(message))
            self.submit.insert(tk.INSERT, message)
            self.submit.pack(side="top")
            row = 1
            self.confirm = tk.Button(self.submit_frame, text="CONFIRM", fg="green",
                                  command=lambda arg1=message:self.confirm_submit(arg1))
            self.confirm.pack(side="left")
            self.reset = tk.Button(self.submit_frame, text="RESET", fg="purple",
                                  command=self.reset_frame)
            self.reset.pack(side="left")
            self.quit = tk.Button(self.submit_frame, text="QUIT", fg="red",
                                  command=self.master.destroy)
            self.quit.pack(side="right")

    def set_user(self, uid, score):
        self.clear_user()
        global curUid, curScore
        curUid = uid
        curScore = int(score)
        self.create_widgets(2)

    def set_trigger(self, trig, pts):
        self.clear_trigger()
        global curTrigger, curPoints
        curTrigger = trig
        curPoints = int(pts)

        self.create_widgets(3)

    def confirm_submit(self, msg):
        global curUid, curScore, curTrigger, curPoints
        message = json.loads(msg)
        request = requests.post("http://71.206.247.211:3000/leaderboard", message).text
        response = requests.post("http://proco.me/data/botw/addlogentry.php", json.dumps(message)).text
        print(response)
        self.reset_frame()


    def reset_frame(self):
        try:
            self.clear_user()
        except:
            idk=1
        try:
            self.clear_trigger()
        except:
            idk=1
        try:
            self.clear_submit()
        except:
            idk=1
        self.create_widgets(1)

    def clear_user(self):
        self.user_frame.destroy()
        self.user_frame = None

    def clear_trigger(self):
        self.trigger_frame.destroy()
        self.trigger_frame = None

    def clear_submit(self):
        self.submit_frame.destroy()
        self.submit_frame = None


root = tk.Tk()
app = Application(master=root)
app.mainloop()