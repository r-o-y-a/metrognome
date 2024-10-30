// http://172.20.10.2:8080/
(
s.waitForBoot {

b = NetAddr.new("127.0.0.1", 57121);
~tempoClock = TempoClock.new(60 / 60);

~beat = Routine({
    loop {
        b.sendMsg("/data", "ping");
        "ping".postln;
        1.wait;
    }
}).play(~tempoClock, quant: 1);


}
);

