# The bible
The project contains full-text of the bible in four (4) translation according to the Catholic Church. It also contains the text of the Catechism of the Catholic Church. This is a part of the scripture-in-action project that I have been working on for several weeks in my spare time.

## the content
It contains for folders for the four translation mentioned above and one folder for the Catechism and one folder for the metadata of the bible. The translations are:

- New American Bible (from the USCCB website)
- Revised Version Edition for Catholic (RSV-CE) (from the EWTN website)
- Douam-Rheims (from http://www.drbo.org)
- Latin Vulgate (from http://www.drbo.org)


```scala
package practices

import scala.io.Source

object FileReader {
  def main(args: Array[String]): Unit = {
//    val fileStream = getClass.getResourceAsStream("/home/student/kiet/thebible/dr/01-Genesis-text.txt")
    val lines = Source.fromFile("/home/student/kiet/thebible/dr/01-Genesis-text.txt").getLines
    lines.foreach(line => {
      var new_line = line
      if (line.size > 0) {
        if (line.startsWith("*** the book")) print("# ")
        else if (line.startsWith("*** chapter")) print("## ")
        else if (!line.charAt(0).isDigit) print("### ")
        else new_line = line + "  "
      }
      println(new_line)
    })
  }
}
```

