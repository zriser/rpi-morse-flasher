import RPi.GPIO as GPIO
import time

try:
	while True:
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(18, GPIO.OUT)

		def blinkdot():
			GPIO.output(18, GPIO.HIGH)
			time.sleep(0.5)
			GPIO.output(18, GPIO.LOW)
			time.sleep(0.5)

		def blinkdash():
			GPIO.output(18, GPIO.HIGH)
			time.sleep(1.5)
			GPIO.output(18, GPIO.LOW)
			time.sleep(0.5)

		def space():
			time.sleep(3.5)

		morse = {'A': '.-','B': '-...','C': '-.-.',
			 'D': '-..','E': '.','F': '..-.',
			 'G': '--.','H': '....','I': '..',
			 'J': '.---','K': '-.-','L': '.-..',
			 'M': '--','N': '-.','O': '---',
			 'P': '.--.','Q': '--.-','R': '.-.',
			 'S': '...','T': '-','U': '..-',
			 'V': '...-','W': '.--','X': '-..-',
			 'Y': '-.--','Z': '--..','0': '-----',
			 '1': '.----',  '2': '..---','3': '...--',
			 '4': '....-','5': '.....','6': '-....',
			 '7': '--...','8': '---..','9': '----.',' ':' '}

		msg = 'happy halloween asymmetrik'
		msg = msg.upper()

		for i in msg:
			blink = morse[i]

			for z in blink:
				if z == '.':
					blinkdot()
				elif z == '-':
					blinkdash()
				else:
					space()

			time.sleep(1.5)

except KeyboardInterrupt:
	print('cleanup!')

finally:
	GPIO.cleanup()
