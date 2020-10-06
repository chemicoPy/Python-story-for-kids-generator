import random

print('Hey Kiddo!. What sort of story would you like to see?')
print('PS: Please keep trying/loading as it takes time to generate another story.')
print('Please choose from this list: { Cars or Countries }')

choice1 = str(input('Enter your choice here:').capitalize())

if choice1== 'Cars' or choice1=='Countries':
    if choice1 == 'Countries':
        choice1_1 = random.choice(
            ['Nigeria', 'USA', 'South Africa', 'Russia', 'Malawi', 'South-Korea', 'Italy', 'Germany', 'The Gambia'])
        choice1_1_1 = random.choice(
            [', a big country where many trees grow', ', a abridged version of a bigger country',
             ', one with many farmlands',
             ', surrounded by many oceans', ', developed country amidst many developing countries',
             ', sub-sahara of limpopo', ', a place of a dense population', ', and flowing with milk and honey'])

        if choice1_1_1 == 'Nigeria' or choice1_1_1 =='The Gambia' or choice1_1_1 =='Malawi' or choice1_1_1 =='South Africa':
            choice1_2 = choice1_1 + choice1_1_1

            year = choice1_2 + (random.choice(['. In', '. Around', '. Late'])) + (random.choice(
                [' 1934', ' 1675', ' 1858', ' 1993', ' 2002', ' 1833', ' 1900', ' 1928', ' 1983', ' 1920', ' 1816',
                 ' 1787', ' 1932',
                 ' 2019', ' 2010', ' 1812']))
            race = random.choice(
                [', The Whites that reside there', ', The neighbouring Africans',
                 ', Subhurb soldiers that live therein']) + (
                       random.choice(['most especially ones older than  ']))
            age = random.randint(0, 100)

            if age >= 50:
                year_race_age = year + race + str(age) + (random.choice(
                    [', they tend to grow weak as the atmosphere of the situations is un-bearing for them',
                     ', their timidity influence actions of their kids/ younger ones',
                     ', migrate to neighboring nations on taking the advice of their wards',
                     ', follow the steps as of the old (ones in their books)']))

                persons = random.choice(
                    ['. Resident workers that were not on strike helped them a lot during the crisis',
                     '. Identified racists did not help matters, they rather compounded the problems',
                     ' . Helps from some non-governmental parastatals were not felt'])

                almost_end = random.choice(['. In the end, ', '. They ultimately ', '. Regretfully, '])
                end1 = year_race_age + persons + almost_end + random.choice(
                    ['had to use their means to get what change they wanted!.', 'found a lasting solution.',
                     'their last resort was to watch as things go.'])

                print('')
                print(end1)
                print('That comes to the end of the brief story on:', choice1_1)
                print('If you enjoyed the story, Kindly run the program again to load another one. Thank You!.')
                print('PS: Please keep trying/loading as it takes time to generate another story.')

            else:
                if age < 50:
                    year_race_age = year + race + str(age) + (random.choice(
                        [', their timidity influence actions of their older ones',
                         ' follow the steps as of the old (ones in their books)',
                         'migrate to neighboring nations on taking the advice of their wards']))

                    persons = random.choice(
                        ['. Resident workers that were not on strike helped them a lot during the crisis',
                         '. Identified racists did not help matters, they rather compounded the problems',
                         '. Helps from some non-governmental parastatals were not felt'])

                    almost_end = random.choice(['. In the end, ', '. Ultimately ', '. Regretfully, '])
                    end1 = year_race_age + persons + almost_end + random.choice(
                        ['had to use their means to get what change they wanted!.', 'found a lasting solution.',
                         'their last resort was to watch as things leave.'])

                    print('')
                    print(end1)
                    print('That comes to the end of the brief story on:', choice1_1)
                    print('If you enjoyed the story, Kindly run the program again to load another one. Thank You!.')
                    print('PS: Please keep trying/loading as it takes time to generate another story.')



        else:
            if choice1_1 == 'USA':
                persons = random.choice([' and the reign of President Stones does not condone such!.',
                                         ' Thankfully, they were in the era of a good man - President Barrack Obama as his help was so immense.'
                                         ' Moreover, the Presidential election was close already!.'])

                year_race_age_persons = (random.choice([' In', ' Around'])) + (random.choice(
                    [' 1934', ' 1675', ' 1858', ' 1993', ' 2002', ' 1833', ' 1900', ' 1928', ' 1983', ' 1920', ' 1816',
                     ' 1787', ' 1932',
                     ' 2019', ' 2010', ' 1812'])) + random.choice(
                    [', The Whites that reside there', ', The neighbouring Africans',
                     ', Sub-hub soldiers that live therein']) + (
                                            random.choice([', most especially ones older than'])) + str(
                    random.randint(0,
                                   100)) + (
                                            random.choice(
                                                [
                                                    ', they tend to grow weak as the atmosphere of the situations is un-bearing for them',
                                                    ', their timidity influence actions of their kids/ younger ones',
                                                    ', migrate to neighboring nations on taking the advice of their wards',
                                                    ', follow the steps as of the old (ones in their books)'])) + persons

                almost_end = random.choice(['. In the end, ', '. Ultimately ', '. Regretfully, '])
                end1 = year_race_age_persons + almost_end + random.choice(
                    [', had to use their means to get the change they wanted!.', ', found a lasting solution.',
                     ', their last resort was to watch as things go.'])

                print('')
                print(end1)
                print('That comes to the end of the brief story on:', choice1_1)
                print('If you enjoyed the story, Kindly run the program again to load another one. Thank You!.')
                print('PS: Please keep trying/loading as it takes time to generate another story.')

            if choice1_1 == 'Italy' or choice1_1 == 'Germany' or choice1_1 == 'South-Korea' or choice1_1 =='Russia':
                year = (random.choice(['In', 'Around', 'Late'])) + (random.choice(
                    [' 1934', ' 1675', ' 1858', ' 1993', ' 2002', ' 1833', ' 1900', ' 1928', ' 1983', ' 1920',
                     ' 1816',
                     ' 1787', ' 1932',
                     ' 2019', ' 2010', ' 1812']))
                race = random.choice(
                    [', The Whites that reside there', ', The neighbouring whites',
                     ', Asian soldiers that live around there']) + (
                           random.choice([', most especially ones older than']))
                age = random.randint(0, 100)

                if age >= 50:
                    year_race_age = year + race + str(age) + (random.choice(
                        [',they tend to grow weak as the atmosphere of the situations is unbearing for them',
                         ', their timidity influence actions of their kids/ younger ones',
                         ', migrate to neighboring nations on taking the advice of their wards',
                         ', follow the steps as of the old (ones in their books)']))

                    persons = random.choice(
                        ['. Resident workers that were not on strike helped them a lot during the crisis',
                         '. Identified racists did not help matters, they rather compounded the problems.',
                         '. Helps from some non-governmental parastatals were not felt'])

                    almost_end = random.choice(['. In the end, ', '. Ultimately ', '. Regretfully, '])
                    end1 = year_race_age + persons + almost_end + random.choice(
                        ['had to use their means to get what change they wanted!.', 'found a lasting solution.',
                         'their last resort was to watch as things go.'])

                    print(end1)
                    print('That comes to the end of the brief story on:', choice1_1)
                    print('If you enjoyed the story, Kindly run the program again to load another one. Thank You!.')
                    print('PS: Please keep trying/loading as it takes time to generate another story.')

                elif age < 50:
                    year_race_age = year + race + str(age) + (random.choice(
                        [', they tend to grow weak as the atmosphere of the situations is unbearing for them',
                         ', their timidity influence actions of their older ones',
                         ' follow the steps as of the old (ones in their books)',
                         ' migrate to neighboring nations on taking the advice of their wards']))

                    persons = random.choice(
                        ['. Resident workers that were not on strike helped them a lot during the crisis',
                         '. Identified racists did not help matters, they rather compounded the problems.',
                         '. Helps from some non-governmental parastatals were not felt'])

                    almost_end = random.choice(['.In the end, ', '. Ultimately ', 'Regretfully, '])
                    end1 = year_race_age + persons + almost_end + random.choice(
                        ['had to use their means to get what change they wanted!.', 'found a lasting solution.',
                         'their last resort was to watch as things flow.'])

                    print('')
                    print(end1)
                    print('That comes to the end of the brief story on:', choice1_1)
                    print('If you enjoyed the story, Kindly run the program again to load another one. Thank You!.')
                    print('PS: Please keep trying/loading as it takes time to generate another story.')









    else:
        if choice1 == 'Cars':
            choice1_1 = random.choice(['Many', 'All but the Old, ', 'Youths, '])

            if choice1_1 == 'Many' or choice1_1 =='Youths':
                age = random.randint(0, 100)

                if age < 30:
                    criteria = choice1_1 + random.choice([', Especially', ', Most likely', ', Usually'])
                    continue1 = random.choice(
                        [' ones that have watched FAST AND FURIOUS', ' Engineering students',
                         ' those that just love them'])
                    continue2 = criteria + continue1

                    almost_end1 = continue2 + random.choice(
                        [' had to use their means to get what they wanted!.',
                         ' found a lasting solution to always have access to them.',
                         ' go as far as borrowing money.', ' request such money from their parents.'])

                    almost_end2 = almost_end1 + random.choice(
                        [' In the end, ', ' They ultimately, ', 'Without regards to nay-sayers, '])
                    end = almost_end2 + random.choice(['had fun!.', 'the lucky ones indeed enjoyed their decisions.',
                                                       'Some regret their decisions anyways!.'])

                    print('')
                    print(end)
                    print('That comes to the end of the brief story on:', 'Cars')
                    print('If you enjoyed the story, Kindly run the program again to load another one. Thank You!.')
                    print('PS: Please keep trying/loading as it takes time to generate another story.')

                if age > 30:
                    criteria = choice1_1 + random.choice([' Especially', ', Most likely', ', Usually'])
                    continue2 = random.choice([', spend their wages/salaries on getting them for themselves. ',
                                               ' those who earn less, buy car toys for their kids. ',
                                               ' go for car-viewing tours '])
                    continue1 = criteria + continue2

                    almost_end1 = continue1 + random.choice(['had to use their means to get what they wanted!',
                                                             'found a lasting solution to always having access to them',
                                                             'go as far as borrowing money'])

                    almost_end2 = almost_end1 + random.choice(
                        ['. In the end, ', '. They ultimately ', '. Without regards to nay-sayers, '])
                    end = almost_end2 + random.choice(
                        ['had their fun!.', 'the lucky ones indeed enjoyed their decisions.',
                         'Some regret their decisions anyways!.'])

                    print('')
                    print(end)
                    print('That comes to the end of the brief story on:', 'Cars')
                    print('If you enjoyed the story, Kindly run the program again to load another one. Thank You!.')
                    print('PS: Please keep trying/loading as it takes time to generate another story.')

            if choice1_1 == 'All but the Old':
                criteria = choice1_1 + random.choice([', Especially', ', Most likely', ', Usually'])
                status = criteria + random.choice(
                    [' ones with kids in senior classes', ' those that have kids in younger classes'])
                continue1 = status + random.choice(
                    [' do not even indulge them with such things', ' advise them strongly against such.',
                     ' did the best they could to sway their attention from cars. '])

                almost_end1 = continue1 + random.choice(
                    ['. In the end, ', '. They ultimately ', '.  Without regards to nay-sayers, '])

                end = almost_end1 + random.choice(
                    [' had their fun!.', 'the lucky ones indeed enjoyed their decisions.',
                     'Some regret their decisions anyways!.', 'their decisions paid off!.',
                     'some lived their lives that way.'])

                print('')
                print(end)
                print('That comes to the end of the brief story on:', 'Cars')
                print('If you enjoyed the story, Kindly run the program again to load another one. Thank You!.')
                print('PS: Please keep trying/loading as it takes time to generate another story.')





else:
    print('Invalid input!. Ensure you choose between Cars or Countries.')







