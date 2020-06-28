available_coins = [1, 2, 5, 10, 20, 50, 100]
change_to_be_made = int(input("enter the change to be made. "))
while change_to_be_made < 0:
    print("change_to_be_made should be positive number ")
    change_to_be_made = int(input("enter the change to be made. "))



def coin_change_for_canonical_coin_system(change_to_be_made, available_coins):
    print(f"coin_change_for_canonical_coin_change is :  ", end="")
    available_coins.reverse()  # to reverse coins in decreasing order
    for coin in available_coins:
        while change_to_be_made >= coin:
            no_of_coins = change_to_be_made // coin
            change_to_be_made = change_to_be_made % coin
            print(f"{no_of_coins} X {coin}$ ,", end="")  # print  every change with its amount



def recive_coins_from_the_user():
    user_coin_list = []
    size = int(input("\nenter the total number of coins you have.  "))
    for i in range(size):
        coin = int(input("enter the coin you left  "))
        while coin < 0:
            print("coin should be positive number  "
                  "please try again")
            coin = int(input("enter the coin you left  "))
        while coin in user_coin_list:
            print("coin should have unique value "
                  "please try again ")
            coin = int(input("enter the coin you left  "))

        user_coin_list.append(coin)  # add coin to user_coin_list

    while 1 not in user_coin_list:  # user try again tofill the coin list again
        print("one coin must have value of 1 !!!"
              "try to add coin '1' try again ")
        recive_coins_from_the_user()

    return user_coin_list  # the list of users coin



def general_case_for_canonical_coin_system(change_to_be_made):
    print("general_case_for_canonical_coin_system_is: ", end="")
    user_coin_list.sort(reverse=True)
    for coin in user_coin_list:
        while change_to_be_made >= coin:
            no_of_coins = change_to_be_made // coin
            change_to_be_made = change_to_be_made % coin
            print(f"{no_of_coins} X {coin}$ ,", end="")  # print  every change with its amount used

    # optimal coin change


def dynamic_approach_for_coin_change(change_to_be_made):
    user_coin_list.sort()  # first sort in increasing order
    minimum_coins = []
    first_coin_index = []
    for i in range(change_to_be_made + 1):  # first fill the two array from 1 to change
        minimum_coins.append(i)
        first_coin_index.append(i)
    for current_change in range(change_to_be_made + 1):  # iterate from 0 to change to be made
        coin_count = current_change  # because dynamic approach starts from the lowest
        # new_coin_index = 0                               # and find the possible answer for the current value
        for i in range(len(user_coin_list)):
            coin = user_coin_list[i]
            if current_change == 0:  # it means we have 0 amount we cant change it just leave it null
                minimum_coins[current_change] = 0
                first_coin_index[current_change] = None
                break
            elif coin == current_change:  # we can make change by it self
                minimum_coins[current_change] = 1
                first_coin_index[current_change] = i
                break
            elif coin > current_change:  # we can't make any different change so we have to break
                break
            elif 1 + minimum_coins[current_change - coin] <= coin_count:  # chuck if it's is lower than what we
                coin_count = 1 + minimum_coins[current_change - coin]  # have before
                new_coin_index = i
                minimum_coins[current_change] = coin_count
                first_coin_index[current_change] = new_coin_index

    def printing_the_optimal_solution_of_coin_change():
        print("The_optimal_solution_of_coin_change_is: ", end="")
        current_change = change_to_be_made
        optimal_coins = []  # the set of all coins used to change
        while current_change > 0:  # ends when we finish  to change all coins
            coin = user_coin_list[first_coin_index[current_change]]
            optimal_coins.append(coin)
            current_change = current_change - coin
        set_optimal_coins = list(set(optimal_coins))  # the set of all coins with out duplicating
        for i in range(len(set_optimal_coins)):  # and sort in increasing order
            print(f"{optimal_coins.count(set_optimal_coins[i])} x {set_optimal_coins[i]}$ ,", end="")

    printing_the_optimal_solution_of_coin_change()  # call the function


# canonical_coin_system
print()
print("\n--------canonical_coin_system--------")
coin_change_for_canonical_coin_system(change_to_be_made, available_coins)
print()
user_coin_list = recive_coins_from_the_user()  # storing all users coin list
print("\n--------general_case_for_canonical_coin_system--------")
general_case_for_canonical_coin_system(change_to_be_made)
print()
print("\n--------dynamic_approach--------")
dynamic_approach_for_coin_change(change_to_be_made)
