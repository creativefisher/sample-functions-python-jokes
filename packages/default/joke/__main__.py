import pyjokes

def main(args):
  joke1 = pyjokes.get_joke()
  joke2 = pyjokes.get_joke()
  joke = joke1 + "\n" +joke2
  return {
    'body': {
      'response_type': 'in_channel',
      'text': joke
    }
  }
