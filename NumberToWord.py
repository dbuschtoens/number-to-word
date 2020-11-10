
ones = [
  " one",
  " two",
  " three",
  " four",
  " five",
  " six",
  " seven",
  " eight",
  " nine",
  " ten",
  " eleven",
  " twelve",
  " thirteen",
  " fourteen",
  " fifteen",
  " sixteen",
  " seventeen",
  " eighteen",
  " nineteen"
]
tens = [
    " twenty",
    " thirty",
    " forty",
    " fifty",
    " sixty",
    " seventy",
    " eighty",
    " ninety"
]
  # the program does not handle numbers larger than quintillions
  # this is ok for now
  #
groups = [
    "",
    " thousand",
    " million",
    " billion",
    " trillion",
    " quadrillion",
    " quintillion"
]

def NumberToWord( n ):
    string = ""
    # Go through the number one group at a time.
    for i in range(len(groups), 0, -1):
      # Is the number as big as this group?
      cutoff = pow( 10, i * 3 )
      if( n >= cutoff ):
        thisPart = ( n / cutoff )
        # Use the ones[] array for both the
        # hundreds and the ones digit. Note
        # that tens[] starts at "twenty".
        if( thisPart >= 100 ):
          string += ones[ thisPart / 100 ] + " hundred"
          thisPart = thisPart % 100
        if( thisPart >= 20 ):
          string += tens[ ( thisPart / 10 ) - 1 ]
          thisPart = thisPart % 10
        if( thisPart >= 1 ):
          string += ones[ thisPart ]
        string += groups[ i ]
        n = n % cutoff
    return string

