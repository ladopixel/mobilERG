# mobilERG

<img src="https://ergonfts.org/other_images/ergo_platform.jpg" alt="Logotipo de Ergo">

## What is it and what can I do with mobilERG?

Before explaining the technology behind this prototype let's see different uses we could give it, I think this way it is much better understood. From now on when I name mobilERG I will be referring to the whole working prototype.

With little knowledge of electronics and a minimum base of programming we can get to give infinite uses. The first thing we must differentiate from mobilERG are 2 very different modes of use:

- Mode 1: mobilERG notifies us that an event has occurred in the distance by means of a call or SMS.
- Mode 2: We make a call or send an SMS to alert mobilERG to start performing a previously defined action.

<hr>

## Mode 1

**I will list some uses to see it clearly so that we can appreciate the potential of Mode 1** (the system is the one who notifies me that an event has occurred):
- Ergo's price goes up and I get an SMS on my personal phone indicating that Ergo is on its way to the moon.
- My Ergo wallet went from having 100 ERG to having 103 ERG.
- Movements at home are detected by a sensor and mobilERG sends me an SMS indicating that there are movements at home.
- Everything that comes to mind...

<hr>

### Mode 2

**List some uses to see clearly and that we can appreciate the potential of Mode 2** (we notify the system so that some action is carried out in the distance):
- Send ERG to a specific wallet.
- Create a token.
- Install the node.
- Last will.
- Turn off the lights at home.
- Computer formatting.
- Anything that comes to mind...

<hr>

**Mode 1**: mobilERG alerts us that something has happened.

**Mode 2**: We alert mobilERG to perform an action.

(**Mode 1** and **Mode 2** alerts can be by phone call or by sending and receiving SMS). 

<hr>

### Development of the example
We will focus for this example on **Mode 2.**

### Can I send 0.01 ERG to a friend's wallet just by making a call or sending an SMS?  
Of course you can, you can do this type of sending and many other actions. 

### Let's see how to send 0.01 ERG to a friend by making a call.

This example could be fully developed with a Raspberry Pi Zero, since it has GPIO for the SIM800L module and the Ergo node versions are incredibly light and fast to synchronize. Although we will leave it for the next example.

Now let's see how to do it using these components:
- Computer.
- Arduino UNO.
- SIM800L.
- SIM card (although it is not mandatory to remove the security PIN, it is easier).
- The ergpy library with which we will interact with the Ergo blockchain (public node).

<hr>

### A brief summary of how mobilERG works:
On one side I have an Arduino with a SIM800L module connected (this module allows to send calls, SMS and receive them). This Arduino by means of AT commands analyzes what happens in the SIM800L module and based on the values (SMS or calls that it sends or receives) sends through the serial port the information that I indicate to it.

On the other hand I have running a mini application written in Python reading the serial port of my computer. Based on the values it receives (values I send from Arduino) I can send ERG, create a token, or whatever I want.

<img src="https://ergonfts.org/other_images/flow-mobilERG.png" alt="mobilERG flow">

<hr>

## Connection for the SIM800L module to our Arduino UNO

**Diode 1N4007** 
This diode will serve to supply the SIM800L module correctly (we subtract 0.7 volts), since we are supplying it with 5 volts and it only needs 4.3 volts.

<img src="https://ergonfts.org/other_images/sim800L-connection.png" alt="Wiring diagram for Arduino and SIM800L">