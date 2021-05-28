start_keyboard = {'inline_keyboard': 
                    [
                        [{'text': 'Показать исходные данные', 'callback_data': 'show_data'}],
                        [{'text': 'Начать поиск паттернов', 'callback_data': 'pattern_search'}]
                    ]
                }

only_search_keyboard = {'inline_keyboard': 
                    [
                        [{'text': 'Начать поиск паттернов', 'callback_data': 'pattern_search'}]
                    ]
                }

continue_keyboard = {'inline_keyboard': 
                    [
                        [{'text': 'Продолжить поиск', 'callback_data': 'continue_search'}],
                        [{'text': 'Прекратить поиск', 'callback_data': 'stop_search'}]
                    ]
                }