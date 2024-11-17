import phrase
import time as timeUtil
from midiutil import MIDIFile

soundCode = 35
bitCode = 34

track = 0
tempo = 60  # In BPM
channel = 9
volume = 127


# Create a midi file from a phrase
def toFile(fileName, myPhrase, metronome=True):
    time = 0
    MyMIDI = MIDIFile(1)  # One track, defaults to format 1 (tempo track is created automatically)
    MyMIDI.addTempo(track, 0, tempo)

    # Configuración del compás (3/4 o 4/4)
    beats_per_measure = 3 if myPhrase.meter == phrase.Meter.TRIPLE else 4
    beat_note = 2  # Negra
    clocks_per_click = 24  # Resolución típica
    thirty_seconds_per_quarter = 8  # Subdivisión típica para la negra
    MyMIDI.addTimeSignature(0, 0, beats_per_measure, beat_note, clocks_per_click, notes_per_quarter=8)

    # Ticks in first measure
    if metronome == True:
        for i in range(beats_per_measure):
            MyMIDI.addNote(track, channel, bitCode, time, 1, volume)
            time += 1

    # Recorrer cada palabra en la frase
    for wordInPhrase in myPhrase.phrase:
        for syllable in wordInPhrase:
            for duration in syllable.getRythm():
                if duration < 0:  # Es un silencio
                    time += abs(duration)  # Solo avanzar el tiempo
                else:  # Es una nota
                    # Si el metrónomo está activo, marca solo si no hay silencio en este beat
                    if metronome and time % 1 == 0:
                        MyMIDI.addNote(track, channel, bitCode, time, 1, volume)
                    # Añadir la nota musical
                    MyMIDI.addNote(track, channel, soundCode, time, duration, volume)
                    time += duration  # Avanzar el tiempo

    # If name is empty geneates a TimeStampName
    if not fileName and not fileName.strip():
        timestr = timeUtil.strftime("%Y%m%d-%H%M%S")
        fileName = "%s-%s" % (timestr, myPhrase.meter.name)

    # Write midi file
    with open(fileName + '.mid', "wb") as output_file:
        MyMIDI.writeFile(output_file)

        # Write text file
    print(myPhrase, file=open(fileName + '.txt', 'w'))

    print('written file to %s' % fileName)


def main():
    myPhraseObj = phrase.Phrase(4, phrase.Meter.DUPLE)  # length:2, meter=DUPLE
    print(myPhraseObj)
    toFile('', myPhraseObj, True)


if __name__ == "__main__":
    main()



