import os
import pickle

from buisness_cards import Buisness_cards
from profile import Profile
from user_peer import User_peer
from worker_information import *


def load(path):
    input = open(path, "rb")
    data = pickle.load(input)
    input.close
    return data


password = "password"

global echange_list
if (os.path.exists("echange_list.pickle")):
    echange_list = load("echange_list.pickle")
else:
    echange_list = []
global current_profile
global buisness_cards


def do_exchanges():
    for peer1 in echange_list:
        for peer2 in echange_list:
            if (peer1.get_user_1() == peer2.get_user_2() and peer1.get_user_2() == peer2.get_user_1()):
                exchanges(peer1.get_user_1(), peer2.get_user_1())


def exchanges(user1, user2):
    if os.path.exists(user1 + ".pickle"):
        if os.path.exists(user2 + ".pickle"):
            data1 = load("name" + ".pickle")
            data2 = load("name2" + ".pickle")
            new_buisness_cards = share_buisness_cards(data1["buisness_cards"], data2["buisness_cards"])
            data1["profil"].add_share_profile(share_profil(data2["profil"]))
            data2["profil"].add_share_profile(share_profil(data1["profil"]))
            save(data1["profil"].get_name() + ".pickle",
                 {"profil": data1["profil"], "buisness_cards": new_buisness_cards})
            save(data2["profil"].get_name() + ".pickle",
                 {"profil": data2["profil"], "buisness_cards": new_buisness_cards})
        else:
            print("error file not exist")
    else:
        print("error file not exist")


def share_profil(profile):
    profile_shared = Worker_information(profile.get_name())
    profile_shared.set_email(profile.get_email())
    profile_shared.set_compagny_name(profile.get_compagny_name())
    profile_shared.set_phone_number(profile.get_phone_number())
    return profile_shared


def share_buisness_cards(buisness_cards1, buisness_cards2):
    for buisness_card1 in buisness_cards1:
        if len(buisness_cards2) > 0:
            not_present = True
        else:
            not_present = False
        for buisness_card2 in buisness_cards2:
            if (buisness_card2.equals(buisness_card1)):
                not_present = False
                break
        if (not_present):
            buisness_cards2.append(buisness_card1)
    return (buisness_cards2)


def set_optional_information(worker_information):
    phone_number = input("Phone number ? (optional) ")
    if (isPhoneNumber(phone_number)):
        worker_information.set_phone_number(phone_number)
    email = input("Email ? (optional) ")
    if (isAnEmail(email)):
        worker_information.set_email(email)
    compagny_name = input("Compagny name ? (optional) ")
    if (compagny_name != ""):
        worker_information.set_compagny_name(compagny_name)


def save(path, data):
    output = open(path, "wb")
    pickle.dump(data, output)
    output.close


def create_new_profile():
    print("Profil creation :")
    incorect_informations = True
    while (incorect_informations):
        name = input("Name ? (mandatory) ")
        if (name != "" and not (os.path.exists(name + ".pickle"))):
            while (incorect_informations):
                proposition_user_password = input("Password ? ")
                if (proposition_user_password != ""):
                    incorect_informations = False
                    current_profile = Profile(name, proposition_user_password)

        else:
            print("Please write a correct name")
    set_optional_information(current_profile)
    return current_profile


def create_buisness_card():
    print("Library interface :\n")
    no_name = True
    print("Add a new buissness card :\n")
    while (no_name):
        name = input("Name ? (mandatory) ")
        if (name != ""):
            no_name = False
            buisness_cards = Buisness_cards(name)
    set_optional_information(buisness_cards)
    return buisness_cards


def get_password_from_file(path):
    input = open(path, "rb")
    data = pickle.load(input)
    input.close
    return data["profil"].get_password()


no_quit = True
while (no_quit):
    do_exchanges()
    no_acces = True
    while (no_acces):
        profile_propsition = input("profile ? ")
        if (profile_propsition == "admin"):
            password_propsition = input("password ? ")
            if (password_propsition == password):
                no_acces = False
                current_profile = Profile("admin", password)
        elif (profile_propsition == "new"):
            current_profile = create_new_profile()
            buisness_cards = []
            save(current_profile.get_name() + ".pickle", {"profil": current_profile, "buisness_cards": buisness_cards})
            no_acces = False
        else:
            if (os.path.exists(profile_propsition + ".pickle")):
                user_password = get_password_from_file(profile_propsition + ".pickle")
                print("Welcome " + profile_propsition)
                user_password_propsition = input("password ? ")
                if (user_password == user_password_propsition):
                    no_acces = False
                    data = load(profile_propsition + ".pickle")
                    current_profile = data["profil"]
                    buisness_cards = data["buisness_cards"]

    repeat = True
    while (repeat):
        action = 0
        action = input(
            "1. add a buisness card\n2. share profil with another user\n3. Show buisness cards \n4. logout\n5. quit\n")
        if (action == "1"):
            buisness_cards.append(create_buisness_card())
        elif (action == "2"):
            user = input("User ? ")
            if (user != "" and os.path.exists(user + ".pickle")):
                echange_list.append(User_peer(current_profile.get_name(), user))
                do_exchanges()
            else:
                print("User doesn't exist")
        elif (action == "3"):
            for buisness_card in buisness_cards:
                print("name " + buisness_card.get_name())
                if buisness_card.get_compagny_name() != None:
                    print("Compagny name " + buisness_card.get_compagny_name())
                if buisness_card.get_email() != None:
                    print("email " + buisness_card.get_email())
                if buisness_card.get_phone_number() != None:
                    print("Phone Number " + buisness_card.get_phone_number())
                print("\n")
        elif (action == "4"):
            repeat = False
            save(current_profile.get_name() + ".pickle", {"profil": current_profile, "buisness_cards": buisness_cards})
        elif (action == "5"):
            no_quit = False
            repeat = False
            save("echange_list.pickle", echange_list)
