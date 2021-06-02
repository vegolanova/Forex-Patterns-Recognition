start_keyboard = {'inline_keyboard':
                  [
                      [{'text': 'Задать процент схожести',
                        'callback_data': 'similarity_percentage'}],
                      [{'text': 'Показать исходные данные',
                        'callback_data': 'show_data'}],
                      [{'text': 'Начать поиск паттернов',
                        'callback_data': 'pattern_search'}]
                  ]
                  }

only_search_keyboard = {'inline_keyboard':
                        [
                            [{'text': 'Начать поиск паттернов',
                              'callback_data': 'pattern_search'}],
                            [{'text': 'Задать процент схожести',
                              'callback_data': 'similarity_percentage'}],
                        ]
                        }
choice_keyboard = {'inline_keyboard':
                   [
                       [{'text': 'Верно', 'callback_data': 'right_percent'}],
                       [{'text': 'Изменить', 'callback_data': 'wrong_percent'}],
                   ]
                   }

continue_keyboard = {'inline_keyboard':
                     [
                         [{'text': 'Продолжить поиск',
                           'callback_data': 'continue_search'}],
                         [{'text': 'Задать процент схожести',
                           'callback_data': 'similarity_percentage'}],
                         [{'text': 'Прекратить поиск', 'callback_data': 'stop_search'}]
                     ]
                     }
