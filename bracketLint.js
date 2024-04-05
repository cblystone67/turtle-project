function bracketLint(string) {
  const openersToClosers = {
    "[": "]",
    "(": ")",
    "{": "}",
  };
  const closersToOpeners = {
    "]": "[",
    ")": "(",
    "}": "{",
  };
  let lines = string.split(/\n/);
  let stack = [];
  let errors = [];
  lines.forEach((line, idx) => {
    line = line.split("");
    for (var i = 0; i < line.length; i++) {
      if (openersToClosers[line[i]]) {
        // Opening bracket
        stack.push(line[i]);
      } else if (closersToOpeners[line[i]]) {
        // Check to see if this closing bracket matches the last opener
        let firstOut = stack.pop();
        if (!firstOut || openersToClosers[firstOut] !== line[i]) {
          errors.push({
            line: idx + 1,
            charIdx: i,
            missing: openersToClosers[firstOut] || closersToOpeners[line[i]],
          });
        }
      }
    }
  });
  while (stack.length) {
    popElement = stack.pop();
    errors.push({
      line: lines.length,
      charIdx: 0,
      missing: openersToClosers[popElement],
    });
  }
  return errors.length ? errors : true;
}