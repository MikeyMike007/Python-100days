// Select relevant DOM elements
const btn_play = document.getElementById('btn_play')
const morse_field = document.getElementById('morse')

var AudioContext = window.AudioContext || window.webkitAudioContext
var ctx = new AudioContext()
var oscillator = ctx.createOscillator()
oscillator.type = 'sine'
oscillator.frequency.value = 600
var dot = 1.2 / 15
var gainNode = ctx.createGain()
oscillator.connect(gainNode)
gainNode.connect(ctx.destination)

btn_play.addEventListener('click', function () {
  var t = ctx.currentTime
  gainNode.gain.setValueAtTime(0, t)

  morse.value.split('').forEach(function (letter) {
    switch (letter) {
      case '.':
        gainNode.gain.setValueAtTime(0.05, t)
        t += dot
        gainNode.gain.setValueAtTime(0, t)
        t += dot
        break
      case '-':
        gainNode.gain.setValueAtTime(0.05, t)
        t += 3 * dot
        gainNode.gain.setValueAtTime(0, t)
        t += dot
        break
      case ' ':
        t += 3 * dot
        break
      case '/':
        t += 7 * dot
        break
    }
  })

  oscillator.start()
  return false
})
