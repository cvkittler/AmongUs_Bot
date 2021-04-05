from screen_search import Search,pyautogui
import time
import numpy as np

def find_task():

    # Download Task
    search_download = Search(r'Tasks\download.PNG')
    
    # card swipe task
    search_wallet = Search(r'Tasks\swipe_card.PNG')

    #fuze task
    search_fuze = Search(r'Tasks\fuze.PNG')

    #sheild task
    search_sheild = Search(r'Tasks\sheild.PNG')
    Point1 = [959, 331]
    Point2 = [788, 453]
    Point3 = [791, 646]
    Point4 = [909, 736]
    Point5 = [1002, 556]
    Point6 = [1155, 600]
    Point7 = [1147, 376]
    sheild_points = [Point1,Point2,Point3,Point4,Point5,Point6,Point7]

    #navagation Task
    search_navagation = Search(r'Tasks\navagation.PNG')
    search_nav_point = Search(r'Tasks\Nav_point.PNG')

    #O2 Filter Task
    search_O2 = Search(r'Tasks\O2_FILTER.PNG')

    #wire Task
    search_wires = Search(r'Tasks\wires.PNG')
    point_w_x = 555
    point_w_y = [275, 461, 645, 830]

    #trash Task
    search_trash = Search(r'Tasks\Trash.png')

    #refuel Task
    search_refuel = Search(r'Tasks\fuel.PNG')
    search_refuel2 = Search(r'Tasks\refuel_eng.PNG')

    #stearing Task
    search_stearing = Search(r'Tasks\stable_stearing.PNG')

    #asreroids Task
    search_asteroids = Search(r'Tasks\asteroids.PNG')

    #samples Task
    search_samples = Search(r'Tasks\samples.PNG')

    #number Task
    search_num_task = Search(r'Tasks\number_game.PNG')

    #engien allinment task
    search_aline_eng = Search(r'Tasks\Lower_eng.PNG',0.9)
    search_aline_eng2 = Search(r'Tasks\upper_eng.PNG',0.9)

    #divert power task
    search_divert_power = Search(r'Tasks\divert_power.PNG')

    #Calibrate Distributor
    search_distributer = Search(r'Tasks\disruptor.PNG')

    pos_download = search_download.imagesearch()
    if pos_download[0] != -1:
        print("DOWNLOAD")
        pyautogui.click(pos_download[0] + 500 , pos_download[1] + 450)
        return
    
    pos_wallet = search_wallet.imagesearch()
    if pos_wallet[0] != -1:
        print("WALLET")
        pyautogui.click(pos_wallet[0] , pos_wallet[1])
        time.sleep(.3)
        pyautogui.click(pos_wallet[0] , pos_wallet[1]-300)
        pyautogui.dragRel(1000, 0, .75)
        return

    pos_fuze = search_fuze.imagesearch()
    if pos_fuze[0] != -1:
         print("FUZE at: ", pos_fuze[0], pos_fuze[1])
         pyautogui.click(pos_fuze[0], pos_fuze[1])

    pos_sheild = search_sheild.imagesearch()
    if pos_sheild[0] != -1:
        print("SHEILD")
        im = pyautogui.screenshot()
        img_rgb = np.array(im)
        #im.save('testarea.png')
        for i in range(-1,6):
            print(img_rgb[sheild_points[i][1], sheild_points[i][0]])
            if (img_rgb[sheild_points[i][1], sheild_points[i][0]][2] < 170):
                pyautogui.click(sheild_points[i][0], sheild_points[i][1])
                time.sleep(.01)

        print('SHEILDS DONE')
        return 

    pos_navagation = search_navagation.imagesearch()
    pos_nav_points = search_nav_point.imagesearch()
    if pos_navagation[0] != -1:
        print('NAVIGATION')
        for i in range(-1,4):
            #while pos_nav_points == -1:
            pos_nav_points = search_nav_point.imagesearch_loop

    #move to [518,539]
    #look in x:694-1400  y:98-980
    pos_O2 = search_O2.imagesearch()
    if pos_O2[0] != -1:
        print('O2')
        im = pyautogui.screenshot()
        img_rgb = np.array(im)
        #im.save('testarea.png'), , 
        for i in range(700,1401, 50):#x axis
            for j in range(100,951,50):
                if img_rgb[j][i][2] < 100:
                    pyautogui.moveTo(i,j)
                    pyautogui.dragTo(518,539,.2)

        print('O2 Done')
        return

    #Do Wires
    pos_wires = search_wires.imagesearch()
    if pos_wires[0] != -1:
        print('WIRES')
        wire_speed = 0.5
        im = pyautogui.screenshot()
        img_rgb = np.array(im)
        current_target = " "

        for i in range(0, 4):
            red = img_rgb[point_w_y[i],point_w_x][0]
            green = img_rgb[point_w_y[i],point_w_x][1]
            blue = img_rgb[point_w_y[i],point_w_x][2] 
            if green > 200: # Yellow
                print(i, ': Yellow')
                current_target = "YELLOW"
            elif blue > 200 and red == 0: #blue
                print(i, ': Blue')
                current_target = "BLUE"
            elif red == 255 and blue == 255: #pink
                print(i, ': Pink')
                current_target = "PINK"
            else:
                print(i, ': Red')
                current_target = "RED"

            for j in range(0, 4):
                red2 = img_rgb[point_w_y[j],1310][0]
                green2 = img_rgb[point_w_y[j],1310][1]
                blue2 = img_rgb[point_w_y[j],1310][2] 

                if (green2 > 200 and current_target == "YELLOW"): # Yellow
                    pyautogui.moveTo(point_w_x, point_w_y[i])
                    pyautogui.dragTo(1330, point_w_y[j],wire_speed)
                elif blue2 > 200 and red2 == 0 and current_target == "BLUE": #Blue
                    pyautogui.moveTo(point_w_x, point_w_y[i])
                    pyautogui.dragTo(1330, point_w_y[j],wire_speed)
                elif red2 == 255 and blue2 == 255 and current_target == "PINK": #pink
                    pyautogui.moveTo(point_w_x, point_w_y[i])
                    pyautogui.dragTo(1330, point_w_y[j],wire_speed)
                elif current_target == "RED" and red2 == 255 and green2 == 0 and blue2 == 0: #Red
                    pyautogui.moveTo(point_w_x, point_w_y[i])
                    pyautogui.dragTo(1330, point_w_y[j],wire_speed)
                    pyautogui.drag
            current_target = " "
        
        return

    pos_trash = search_trash.imagesearch()
    if pos_trash[0] != -1:
        print("TRASH")
        pyautogui.moveTo(1272,417)
        pyautogui.mouseDown()
        pyautogui.moveTo(1272,1080.25)
        time.sleep(1.5)
        pyautogui.mouseUp()
        return

    pos_refuel = search_refuel.imagesearch()
    if pos_refuel[0] != -1:
        print("REFUEL")
        pyautogui.moveTo(1460,880)
        pyautogui.mouseDown()
        time.sleep(3)
        pyautogui.mouseUp()
        return

    pos_refuel2 = search_refuel2.imagesearch()
    if pos_refuel2[0] != -1:
        print("FILLING ENG")
        pyautogui.moveTo(1460,880)
        pyautogui.mouseDown()
        time.sleep(3.)
        pyautogui.mouseUp()
        return

    pos_stearing = search_stearing.imagesearch()
    if pos_stearing[0] != -1:
        print("STABLE STEARING")
        pyautogui.moveTo(pos_stearing[0] + 80, pos_stearing[1] + 80)
        pyautogui.dragTo(960,540,.4)
        return

    #click between x:1330 y:150-900
    pos_asteroids = search_asteroids.imagesearch()
    if pos_asteroids[0] != -1:
        print("ASTEROIDS")
        done = False
        while not done:
            for i in range(150,901, 100):
                pyautogui.click(1330, i)
            pos_asteroids = search_asteroids.imagesearch()
            if pos_asteroids[0] == -1:
                done = True
        return

    pos_samples = search_samples.imagesearch()
    if pos_samples[0] != -1:
        print("SAMPLES")
        pyautogui.click(1250, 940)
        time.sleep(0.01)
        pyautogui.click(471,134)
        return

    pos_num_game = search_num_task.imagesearch()
    if pos_num_game[0] != -1:
        print("NUMBER GAME")
        for i in range(1,11):
            path = r'Tasks\number_buttons\_num' + str(i) + '.PNG'
            cur_num = Search(path)
            pos_num_game = cur_num.imagesearch()
            pyautogui.click(pos_num_game[0] + 20,pos_num_game[1] + 20)
            time.sleep(0.005)
        return

    pos_divert_power = search_divert_power.imagesearch()
    if pos_divert_power[0] != -1:
        print('DIVERTING POWER')
        pyautogui.moveTo(pos_divert_power[0],pos_divert_power[1])
        pyautogui.dragRel(0, 300, 0.1)
        return

    pos_aline_eng = search_aline_eng.imagesearch()
    pos_aline_eng2 = search_aline_eng2.imagesearch()
    if pos_aline_eng[0] != -1 or pos_aline_eng2[0] != -1:
        print("ALINE ENGEIN")
        im = pyautogui.screenshot()
        img_rgb = np.array(im)
        for i in range(1187,1380,5):#x
            for j in range(134,950,5):#y
                #pyautogui.moveTo(i,j) 
                red = img_rgb[j,i][0]
                green = img_rgb[j,i][1]
                if(red == 88 and green == 88):
                    print('found neadle')
                    pyautogui.moveTo(i,j)
                    pyautogui.mouseDown()
                    pyautogui.moveTo(1242,537,0.2)
                    time.sleep(0.01)
                    pyautogui.mouseUp()
                    pos_aline_eng = [-1,-1]
                    pos_aline_eng2 = [-1,-1]
                    return

        return
    
    pos_distributers = search_distributer.imagesearch()
    check_locations = [[800,297],[800,572],[800,851]]
    click_locations = [[1234,309],[1230,585],[1230,841]]

    if pos_distributers[0] != -1:
        print("DISTRIBUTER")
        im = pyautogui.screenshot()
        img_rgb = np.array(im)
        while pos_distributers[0] != -1:#230,495,766
            for i in range(0,3):
                print(i)
                waiting = True
                while waiting:
                    if img_rgb[check_locations[i][1],check_locations[i][0]][1] < 80:
                        time.sleep(0.05)
                        pyautogui.click(click_locations[i][0],click_locations[i][1])
                        time.sleep(0.3)
                        pos_distributers = search_distributer.imagesearch()
                        waiting = False
                    im = pyautogui.screenshot()
                    img_rgb = np.array(im)
            
        return


