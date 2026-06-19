import json
import emoji
class Game:
    def __init__(self):
        self.errors = []
        self.records = None
        self.challenges = None
        self.achievements_data = None
        self.unlocked_difficulties = []
        self.coins = 0
        with open('firstinfo.json', 'r') as f:
            self.first_time = json.load(f)["First Time"]
        if self.first_time:
            with open('challenges_data.json', 'w') as f:
                data = {
                    "Begginer-C 001": {
                        "Name": "First Win!",
                        "Doc": "Get your first win to win this challenge!",
                        "Reward": "20 Coins" ,
                        "Wins": 0
                        },
                    "Beginer-C 002": {
                      "Name": "First Lose!:",
                      "Doc": "Lose One Time!",
                      "Reward": "5 Coins",
                      "Loses": 0
                        }
                    }
                json.dump(data, f, ensure_ascii=False, indent=4)
                with open("firstinfo.json", 'w') as fi_f:
                    json.dump({"First Time": False}, fi_f, indent=2)
            with open('achievements_data.json', 'w') as ad_f:
                json.dump({}, ad_f, indent=2)
    def load_data(self):
        print(emoji.emojize(":mag: Loading data...", language='alias'))
        try:
            with open('records_data.json', 'r') as f:
                records_data = json.load(f)
            required_keys = ["Wrong Guesses", "Remaining Guesses", "Difficulty", "Average"]
            for record, record_data in records_data.items():
                for key in required_keys:
                    if key not in record_data:
                        self.errors.append(f"{record} Has unknown data.Could not found {key}.Details: {record_data}")
                        print(emoji.emojize(f":cross_mark: {record} Has Unknown Data.", language = 'alias'))
            self.records = records_data
            print(emoji.emojize(":white_check_mark: Records data loaded.", language = 'alias'))
        except json.JSONDecodeError:
            print(emoji.emojize(":cross_mark: Record data is corrupted!", language='alias'))
            self.errors.append("Record Data Is Corrupted")
        except FileNotFoundError:
            print(emoji.emojize(":warning: It is like you dont have any records!", language='alias'))
        try:
            with open('challenges_data.json', 'r') as f:
                challenges_data = json.load(f)
            required_keys = ["Name", "Doc", "Reward"]
            for challenge, challenge_data in challenges_data.items():
                for key in required_keys:
                    if key not in challenge_data:
                        self.errors.append(f"{challenge} Has Unknown Data.Could not found {key}.Details: {challenge_data}")
                        print(emoji.emojize(f":cross_mark: {challenge} Has Unknown Data.", language = "alias"))
            self.challenges = challenges_data
            print(emoji.emojize(":white_check_mark: Challenges data loaded.", language = "alias"))
        except json.JSONDecodeError:
            print(emoji.emojize(":cross_mark: Challenges data is corrupted", language = "alias"))
            self.errors.append("Challenges Data Is Corrupted")
        except FileNotFoundError:
            print(emoji.emojize(":cross_mark: Could not find challenges data!", language='alias'))
            self.errors.append("Challenges Data File Not Found")
        try:
            with open("achievements_data.json", 'r') as f:
                achievements_data = json.load(f)
            required_keys = ["Name", "Doc"]
            for achievement, achievement_data in achievements_data.items():
                for keys in required_keys:
                    if key not in required_keys:
                        self.errors.append(f"{achievement} has unknown data.Could not found {key}.Details: {achievement_data}")
                        print(emoji.emojize(f":cross_mark: {achievement} has unknown data!", language = 'alias'))
            print(emoji.emojize(":white_check_mark: Achievements data loaded.", language = 'alias'))
        except json.JSONDecodeError:
            print(emoji.emojize(":cross_mark: Achievements data is corrupted!", language = 'alias'))
            self.errors.append("Achievements Data Is Corrputed")
        except FileNotFoundError:
            print(emoji.emojize(":warning: It is like you don't have any achievements", language = 'alias'))
            self.errors.append("Achievements Data File Not Found")
        if self.errors:
            print(emoji.emojize(":mag: There Is Some Errors! Are you sure you want to continue:question:", language='alias'))
            continue_question = input("[Details, No] (Default: No): ").lower()
            if continue_question == "details":
                for error in self.errors:
                    print(error)
                while True:
                    question = input("What Do You Want To Do?[1)Contact Support, 2)Exit](default: Exit): ")
                    if question == "1":
                        print("""
    Please, first read guide in rubika channel: @GNTL_guide
    If guid didn't help, contact support with email.
    Support's Email: gtnl_support@gmail.com
                              """)
                        input("\nPress Enter To Continue...")
                        continue
                    elif question == "DEV MODE":
                        return "Developer Mode Requested"
                    else:
                        return False
                    
            else:
                return False
        return True
    def menu(self):
        while True:
            print(f"""
Guess The Number - Advanced | V Alpha 0.1
{"=" * 50}
Coins: {self.coins}
Choose a difficulty or a option.
--------
Difficulties
----
1)Easy(1-20) - 15 Guesses - 5 Coins
2)Normal(1-100) - 10 Guesses {"" if "normal" in self.unlocked_difficulties else "(Locked)"} - 10 Coins
3)Hard(1-1_000) - 10 Guesses {"" if "hard" in self.unlocked_difficulties else "(Locked)"} - 20 Coins
4)Expert(1-10_000) - 13 Guesses {"" if "expert" in self.unlocked_difficulties else "(Locked)"} - 40 Coins
5)Nightmare(1-100_000) - 10 Guesses {"" if "nightmare" in self.unlocked_difficulties else "(Locked)"} - 80 Coins
6)Impossible(1-1_000_000) - 12 Guesses {"" if "impossible" in self.unlocked_difficulties else "(Locked)"} - 160 Coins
------
Options
----
7)Challenges
8)Achievements
9)Records
10)Update News
11)Exit
    """)
            choose = input("Please choose a number(1-10): ")
            if choose == "1":
                return {"Easy": {"Guesses": 15, "Reward": 5}}
            elif choose == "2":
                if "normal" not in self.unlocked_difficulties:
                    unlock = input(emoji.emojize(":warning: This difficulty is locked! Are you sure you want to unlock it[y,n]?(50 Coins): ", language = 'alias'))
                    if unlock == "y":
                        if self.coins < 50:
                            print(emoji.emojize(":coin: Your coins aren't enough to buy Normal difficulty!"))
                            input("Press enter to continue...")
                            continue
                        self.unlocked_difficulties.append("normal")
                        print(emoji.emojize(":with_check_mark: Successfully buyed Normal difficulty!"))
                        input("Press enter to continue...")
                        continue
            elif choose == "3":
                pass
        
