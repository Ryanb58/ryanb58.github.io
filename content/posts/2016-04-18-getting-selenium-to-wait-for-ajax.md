title = "Getting Selenium To Wait For Ajax"
date = 2016-04-18T17:47:00+02:00
tags = [
    "ajax",
    "selenium",
    "splinter",
    "success"
]
published = true
+++++

Recently, my buddy [David](http://davidgalitsky.com/) and I were getting frustrated with some selenium tests. The issue being that we run into several cases where Ajax calls are still being ran while selenium is trying to move on to the next line of code.

Finally, we figured out the solution below. Basically, what it does is return a Boolean based on the amount of active jQuery Ajax calls that are going on right now. When the boolean is True the WebDriverWait function allows us to move along in our code. It is a simple, but necessary evil to get selenium tests to work as expected.

```
from selenium.webdriver.support.ui import WebDriverWait
WebDriverWait(self.driver, 5).until(lambda x: self.driver.execute_script("return $.active == 0"))</pre>
```

** Note requires jQuery