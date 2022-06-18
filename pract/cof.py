# 5302087997:AAGTWXMQS4lJT3WVQMT_PTc2xMlwfiSBR60
# coffee recipes coffeerecip_bot t.me/coffeerecip_bot
import telebot
from telebot import types

token = '5302087997:AAGTWXMQS4lJT3WVQMT_PTc2xMlwfiSBR60'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_bot(message):
    bot.send_message(message.chat.id, "Good morning. Choose which coffee you'd like to prepare today? Choose: ",
                     reply_markup=create_keyboard_st())


def create_keyboard_st():
    keyboard1 = types.InlineKeyboardMarkup()
    national_rec = types.InlineKeyboardButton(text='National coffee recipes', callback_data='1')
    based_on_exp = types.InlineKeyboardButton(text='Based on the expresso', callback_data='2')
    iced_coffee = types.InlineKeyboardButton(text='Iced coffee', callback_data='3')
    coffee_with = types.InlineKeyboardButton(text='Coffee with additives', callback_data='4')
    keyboard1.add(national_rec)
    keyboard1.add(based_on_exp)
    keyboard1.add(iced_coffee)
    keyboard1.add(coffee_with)
    return keyboard1


def create_keyboard_return():
    keyboard_return = types.InlineKeyboardMarkup()
    return_ = types.InlineKeyboardButton(text='Back', callback_data='5')
    keyboard_return.add(return_)
    return keyboard_return


def create_keyboard_nr():
    keyboard_nr = types.InlineKeyboardMarkup()
    arabian_c = types.InlineKeyboardButton(text='Arabian coffee', callback_data='6')
    brazil_c = types.InlineKeyboardButton(text='Brazilian coffee', callback_data='7')
    french_c = types.InlineKeyboardButton(text='French coffee', callback_data='8')
    irish_c = types.InlineKeyboardButton(text='Irish coffee', callback_data='9')
    keyboard_nr.add(arabian_c)
    keyboard_nr.add(brazil_c)
    keyboard_nr.add(french_c)
    keyboard_nr.add(irish_c)
    return keyboard_nr


def create_keyboard_bone():
    keyboard_expr = types.InlineKeyboardMarkup()
    amer_btn = types.InlineKeyboardButton(text='Caffe Americano', callback_data='10')
    latte_btn = types.InlineKeyboardButton(text='Caffe Latte', callback_data='11')
    cap_btn = types.InlineKeyboardButton(text='Cappuccino', callback_data='12')
    mocha_btn = types.InlineKeyboardButton(text='Mochaccino', callback_data='13')
    keyboard_expr.add(amer_btn)
    keyboard_expr.add(latte_btn)
    keyboard_expr.add(cap_btn)
    keyboard_expr.add(mocha_btn)
    return keyboard_expr


def create_keyboard_ic():
    keyboard_ic = types.InlineKeyboardMarkup()
    ic_eng = types.InlineKeyboardButton(text="Iced-coffee 'English'", callback_data='14')
    ifm = types.InlineKeyboardButton(text='Irish frozen Mocha', callback_data='15')
    ic_fresh = types.InlineKeyboardButton(text="Iced-coffee 'Freshness'", callback_data='16')
    ic_eli = types.InlineKeyboardButton(text="Iced-coffee 'Elicxir'", callback_data='17')
    keyboard_ic.add(ic_eng)
    keyboard_ic.add(ifm)
    keyboard_ic.add(ic_fresh)
    keyboard_ic.add(ic_eli)
    return keyboard_ic


def create_keyboard_cw():
    keyboard_cw = types.InlineKeyboardMarkup()
    cwp = types.InlineKeyboardButton(text="Coffee with peper", callback_data='18')
    cp = types.InlineKeyboardButton(text='Coffee punch', callback_data='19')
    c_holly = types.InlineKeyboardButton(text="Coffee 'Hollywood'", callback_data='20')
    keyboard_cw.add(cwp)
    keyboard_cw.add(cp)
    keyboard_cw.add(c_holly)
    return keyboard_cw


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    keyboard_2 = create_keyboard_nr()
    keyboard_3 = create_keyboard_return()
    if call.message:
        if call.data == '1':
            create_keyboard_nr()
            bot.send_message(chat_id=call.message.chat.id, text="Choose the recipe", reply_markup=keyboard_2)
        elif call.data == '2':
            create_keyboard_bone()
            bot.send_message(chat_id=call.message.chat.id, text="Choose the recipe",
                             reply_markup=create_keyboard_bone())
        elif call.data == '3':
            create_keyboard_ic()
            bot.send_message(chat_id=call.message.chat.id, text="Choose the recipe",
                             reply_markup=create_keyboard_ic())
        elif call.data == '4':
            create_keyboard_cw()
            bot.send_message(chat_id=call.message.chat.id, text="Choose the recipe",
                             reply_markup=create_keyboard_cw())
        elif call.data == '5':
            create_keyboard_return()
            bot.send_message(chat_id=call.message.chat.id, text="Choose the recipe",
                             reply_markup=create_keyboard_st())
        elif call.data == '6':
            img_arab = open('arab_c.jpeg', 'rb')
            bot.send_photo(chat_id=call.message.chat.id, photo=img_arab, caption='Arabian coffee.', )
            bot.send_message(chat_id=call.message.chat.id,
                             text='''Ingredients: 
            1. 1 pint water; 
            2. 3 tablespoons ground coffee; 
            3. 3 tablespoons sugar;
            4. 1/4 teaspoon cinnamon;
            5.1/4 teaspoon cardamon;
            6.1teaspoon vanilla.
            Preparation:
            all ingredients in a saucepan until foam starts to form on top. 
            Serve immidietly.''', reply_markup=keyboard_3)
            img_arab.close()
        elif call.data == '7':
            img_b = open('brazil.jpg', 'rb')
            bot.send_photo(chat_id=call.message.chat.id, photo=img_b, caption='Brazilian coffee')
            bot.send_message(chat_id=call.message.chat.id,
                             text='''Ingredients:
            1. 4 cups hot chocolate;
            2. 1,5 cups of strong coffee;
            3. 1 cup brandy or rum;
            4. 0,5 cup heavy cream whipped with 1 teaspoon sugar;
            Preparation:
            1. heat the chocolate, coffee and brandy or rum together.
            2. fold in whipped cream (or place a spoonful on top of each serving.''', reply_markup=keyboard_3)
            img_b.close()
        elif call.data == '8':
            img_f = open('french.jpg', 'rb')
            bot.send_photo(chat_id=call.message.chat.id, photo=img_f, caption='French coffee')
            bot.send_message(chat_id=call.message.chat.id,
                             text='''Ingredients:
            1. 6 teaspoons of coffee of fine grind ;
            2. 4 cups of boiled water;
            3. salt pinch;
            4. black ground pepper on a knife tip;
            5 1 wine-glass of the French cognac;
            6. sugar to taste.
            Preparation:
            prepare black coffee, filter and add a little salt and ground pepper.''', reply_markup=keyboard_3)
            img_f.close()
        elif call.data == '9':
            img_i = open('irish.jpg', 'rb')
            bot.send_photo(chat_id=call.message.chat.id, photo=img_i, caption='Irish coffee')
            bot.send_message(chat_id=call.message.chat.id,
                             text='''Ingredients:
            1. 1 cup of hot gourmet coffee;
            2. 1 shot of Irish whiskey;
            Preparation:
            1. mix Irish Whiskey and hot gourmet coffee.
            2. You can top it with whipped cream.''', reply_markup=keyboard_3)
            img_i.close()
        elif call.data == '10':
            img_am = open('americano.jpg', 'rb')
            bot.send_photo(chat_id=call.message.chat.id, photo=img_am, caption='Cafe Americano')
            bot.send_message(chat_id=call.message.chat.id,
                             text='''Ingredients:
            1. espresso;
            2. hot water;
            Preparation:
            1. extract espresso shot directly into cup.
            # 2. fill cup with hot water, leaving enough place for cream if desired and serve.''',
                             reply_markup=keyboard_3)
            img_am.close()
        elif call.data == '11':
            img_lat = open('latte.jpg', 'rb')
            bot.send_photo(chat_id=call.message.chat.id, photo=img_lat, caption='Cafe Latte')
            bot.send_message(chat_id=call.message.chat.id,
                             text='''Ingredients:
                                 1. 2 cups milk;
                                 2. 1,5 cups hot freshly brewed dark roast espresso coffee;
                                 Preparation:
                                 Heat milk in a saucepan set over medium-low heat.
                                 Whisk briskly with a wire whisk to create foam.
                                 Brew espresso and pour into 4 cups.
                                 Pour in milk, holding back the foam with a spoon.
                                 Spoon foam over the top.''', reply_markup=keyboard_3)
            img_lat.close()
        elif call.data == '12':
            img_cap = open('cappuc.jpg', 'rb')
            bot.send_photo(chat_id=call.message.chat.id, photo=img_cap, caption='Cappuccino')
            bot.send_message(chat_id=call.message.chat.id,
                             text='''Ingredients:
            1. 2 tablespoons finely ground dark roast coffee;
            2. 4 ounces water;
            3. 4 ounces milk;
            Preparation:
            Pull a Double Shot of Espresso. Foam the Milk.
            Top the espresso with foamed milk right after foaming.''', reply_markup=keyboard_3)
            img_cap.close()
        elif call.data == '13':
            img_moc = open('mocc.jpg', 'rb')
            bot.send_photo(chat_id=call.message.chat.id, photo=img_moc, caption='Mochaccino')
            bot.send_message(chat_id=call.message.chat.id,
                             text='''Ingredients:
                                 1. ¾ cup milk;
                                 2. 1 tablespoon white sugar;
                                 3. 1 teaspoon instant coffee granules;
                                 4. 1 teaspoon cocoa powder;
                                 5. ½ teaspoon vanilla extract;
                                 6. 1 tablespoon chocolate syrup;
                                 7. 1 tablespoon whipped cream.
                                 ''')
            bot.send_message(chat_id=call.message.chat.id,
                             text='''Preparation:
                                    Blend milk, sugar, instant coffee granules, cocoa powder, and vanilla extract in
                                    a blender until smooth.
                                    Lightly coat the inside of a glass with chocolate syrup.
                                    Pour the coffee mixture into the glass.
                                    Top with whipped cream to serve''', reply_markup=keyboard_3)
            img_moc.close()
        elif call.data == '14':
            img_eng = open('Eng.jpg', 'rb')
            bot.send_photo(chat_id=call.message.chat.id, photo=img_eng, caption='''Iced coffee 'English''')
            bot.send_message(chat_id=call.message.chat.id,
                             text='''Ingredients:
                                 1. 60 g of ground coffee;
                                 2. 4 scopes of ice-cream;
                                 3. 150 g of cream;
                                 4. 400 ml of boiled water.
                                 Preparation:
                                 Brew ordinary Turkish coffee, filter and cool it.
                                 The cooled coffee mix with ice-cream and cream and puor into glasses. ''',
                             reply_markup=keyboard_3)
            img_eng.close()
        elif call.data == '15':
            img_ifm = open('ifm.jpg', 'rb')
            bot.send_photo(chat_id=call.message.chat.id, photo=img_ifm, caption='Irish frozen Mocha')
            bot.send_message(chat_id=call.message.chat.id,
                             text='''Ingredients:
                                 1. 0,5 cups of just brewed strong coffee;
                                 2. 1 cup of milk;
                                 3. 1 cup of liquor Baileys;
                                 4. 4 teaspoons of cocoa powder.
                                 Preparation:
                                 Mix coffee, milk, cocoa in small capacity and heat up until cocoa will completely
                                 dissolve.
                                 Allow a drink to cool down, then add in it half-cup of liquor ‘Baileys’,
                                  mix, fill in capacity for ice and put in the refrigerator for freezing.
                                  After that ice cubes put in a blender, fill in with remained liquor and
                                  grind before formation of a small ice crumb (not to grind completely). Serve in high
                                  glasses.''', reply_markup=keyboard_3)
            img_ifm.close()
        elif call.data == '16':
            img_fresh = open('freshness.jpg', 'rb')
            bot.send_photo(chat_id=call.message.chat.id, photo=img_fresh, caption='Iced coffee "Freshness"')
            bot.send_message(chat_id=call.message.chat.id,
                             text='''Ingredients:
                                 1. 4 cups of strong coffee;
                                 2. 3 table spoons of honey;
                                 3. 30 g. of sugar;
                                 4. Lemon (at will);
                                 5. Egg yolk (at will).''')
            bot.send_message(chat_id=call.message.chat.id,
                             text='''Preparation:
                             Honey and sugar is dissolved in coffee.
                             Then add milk and cream.
                             Turned out drink should be cooled, then poured into glasses with ice-cream.
                             For improvement of taste of a drink it is possible to add lemon juice and the shaken up
                             yolk.''', reply_markup=keyboard_3)
            img_fresh.close()
        elif call.data == '17':
            img_el = open('elixir.jpg', 'rb')
            bot.send_photo(chat_id=call.message.chat.id, photo=img_el, caption='''Coffee 'Elixir''')
            bot.send_message(chat_id=call.message.chat.id,
                             text='''Ingredients:
                                 1. 100 g coffee of fine grind;
                                 2. 0,25 l of water;
                                 3. 250 g of whipped cream;
                                 4. 100 g of powdered sugar;
                                 5. 3 egg yolks.
                                 Preparation:
                                 Make Turkish coffee with sugar and cool it.
                                 Add whipped cream: shake up yolks before formation of foam and add
                                 sour milk which also has been shaken up to a consistance of a cream.''',
                             reply_markup=keyboard_3)
            img_el.close()
        elif call.data == '18':
            img_p = open('with p.jpeg', 'rb')
            bot.send_photo(chat_id=call.message.chat.id, photo=img_p, caption='Coffee with pepper')
            bot.send_message(chat_id=call.message.chat.id,
                             text='''Ingredients:
                                 1 . 5-6 teaspoons of ground coffee;
                                 2. 1-1,5 g. of Black pepper;
                                 3. 0,5 l of cold water.
                                 ''')
            bot.send_message(chat_id=call.message.chat.id,
                             text='''Preparation:
                             The coffee pot is warm up on fire, filled with black pepper and ground coffee.
                             Mix and fill in with cold water (100 ml).
                             Lead up to boiling and without allowing coffee to boil, add 150 more ml of water,
                             again lead up to boiling. Then add the remained water (250 ml) and repeat the procedure
                             once again.
                             Remove from fire and 5-7 minutes allow coffee to be drawn.''', reply_markup=keyboard_3)
            img_p.close()
        elif call.data == '19':
            img_punch = open('punch.jpg', 'rb')
            bot.send_photo(chat_id=call.message.chat.id, photo=img_punch, caption='Coffee punch')
            bot.send_message(chat_id=call.message.chat.id,
                             text='''Ingredients:
                                 1. 60 g of ground coffee;
                                 2. 4 cups of hot water;
                                 3. 8 teaspoons of sugar;
                                 4. 8 pieces of cloves;
                                 5. 4 slices of a stick of cinnamon;
                                 6. 1 small wine-glass of rum.
                                 Preparation:
                                 Coffee is filled in with hot water and spilled in preliminary warmed cups.
                                 In each cup 2 cloves and 1 slice of a cinnamon stick is put on, then poured warmed rum.
                                 In a ready drink put sugar to taste and serve it hot.''', reply_markup=keyboard_3)
            img_punch.close()
        elif call.data == '20':
            img_holly = open('holly.jpg', 'rb')
            bot.send_photo(chat_id=call.message.chat.id, photo=img_holly, caption='Coffee "Hollywood"')
            bot.send_message(chat_id=call.message.chat.id,
                             text='''Ingredients:
                                 1. 2 cups of very strong coffee;
                                 2. 2 tablespoons of cocoa;
                                 3. 2 tablespoons of powdered sugar;
                                 4. 2 cups of milk;
                                 5. Fried almonds.
                                 Preparation:
                                 Make very strong coffee, separately boil milk.Put into a pan of cocoa and sugar,
                                 pour there a part of milk and well mix, and then add the remained milk and a salt
                                 pinch.
                                 Put on fire and boil approximately 10 minutes.Remove from fire,
                                 vigorously shake up before reception of oily, bubbling weight after that add coffee,
                                 continuing to shake up.
                                 Then a hot drink spill in cups and decorate with whipped cream.
                                 It is recommended to strew cream with fried almonds.''', reply_markup=keyboard_3)
            img_holly.close()


if __name__ == '__main__':
    bot.polling(none_stop=True)
