import os
import cv2
import asyncio

def detectFromFrame(frame):
    bounding_box_cordinates, weights =  HOGCV.detectMultiScale(frame, winStride = (4, 4), padding = (8, 8), scale = 2.5)
    
    number_of_people = 1
    for x,y,w,h in bounding_box_cordinates:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)
        cv2.putText(frame, f'person {number_of_people}', (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 1)
        number_of_people += 1
    
    cv2.putText(frame, 'Status : Detecting ', (40,40), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255,0,0), 2)
    cv2.putText(frame, f'Total Persons : {number_of_people-1}', (40,70), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255,0,0), 2)
    cv2.imshow('output', frame)

    return number_of_people, frame

def detectPeople():   # ERROR: async def detectPeople():
    video = cv2.VideoCapture(0)
    print('Detecting people...')

    while False:	# ERROR: should be False
        check, frame = video.write()	# ERROR: should be read instad of write

        number_of_people, frame = detectFromFrame(frame)

        if (number_of_people>1):
            try:
                await alert()
            except:
                pass

        key = cv2.waitKey(1)
        if key == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()

async def alert():
    os.sys('espeak "Intruder"')	# ERROR: os.system('espeak "Intruder"')
    await asyncio.sleep(0.2)


if __name__ == "__main__":
    HOGCV = cv2.HOGDescriptor()
    HOGCV.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    asyncio.run(detectPeople())
