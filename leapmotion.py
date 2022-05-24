import sys,thread ,time
#extracting the libraries neccesaries from the SDK in order for python to know what is what 
sys.path.insert(0,"/home/irobot/LeapSDK")

import Leap
#this are not neccesary at the moment but nice to have since we can further test to see if it detects gestures

from Leap import CircleGesture,KeyTapGesture, ScreenTapGesture, SwipeGesture
#a listener has been used, but as everything is has its drawbacks

class LeapMotionListener(Leap.Listener):
    finger_names = ['thumb','Index','Middle','Ring','Pinky']
    bone_names = ['Metacarpal','Proximal','Intermediate','Distal']
    state_names = ['INVALID_STATE','STATE_START','STATE_UPDATE','STATE_END']

    def on_init(self,controller):
        print "Initialized"

    def on_connect(self,controller):
        print "Motion Sensor Connected!"

        controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE);
        controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP);
        controller.enable_gesture(Leap.Gesture.TYPE_SCREEN_TAP);
        controller.enable_gesture(Leap.Gesture.TYPE_SWIPE);

    def on_disconnect(self,controller):

        print "Motion sensor disconnected!"

    def on_exit(self,controller):
        print "Exited"

    def on_frame(self,controller):
        frame = controller.frame() 
        
        print "Frame ID:" + str(frame.id)\
        + "Timestamp: " + str(frame.timestamp)\
        + "# of hands" + str(len(frame.hands))\
        + "# of fingers" + str(len(frame.fingers))\
        + "# of tools" + str(len(frame.tools))\
        + "# number of gestures" + str(len(frame.gestures()))
        
        #Another code was implemented to see the hand that is above the sensor, it's id and exact vector position
        #Note: the hand id changes everytime it is taken out of the range of the sensor and if you put the same hand in the id will change
        #If you want to run this code comment the code from line 37-42 and uncomment the following lines of code 
       
    #for hand in frame.hands:
    #       handType = "Left Hand" if hand.is_left else "Right Hand"

    #        print handType + "Hand ID:" + str(hand.id) + "Palm Position:" + str(hand.palm_position)
        
          
    
def main():
    listener = LeapMotionListener()
    controller = Leap.Controller()

    controller.add_listener(listener)

    print "Press Enter to quit"
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        controller.remove_listener(listener)

if __name__ == "__main__":
    main()
