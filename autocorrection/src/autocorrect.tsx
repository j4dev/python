import React, { useState, ChangeEvent, FC } from 'react';

interface AutocorrectTextareaProps {
  corrections: { [key: string]: string };
}
const AutocorrectTextarea: FC<AutocorrectTextareaProps> = ({ corrections }) => {

  const [text, setText] = useState<string>('');

  const handleChange = (event: ChangeEvent<HTMLTextAreaElement>) => {
    const value = event.target.value;

    if (value.endsWith(' ')) {
      const words = value.trim().split(' ');
      const lastWord = words[words.length - 1];

      if (corrections[lastWord]) {
        words[words.length - 1] = corrections[lastWord];
      }

      setText(words.join(' ') + ' ');
    } else {
      setText(value);
    }
  };

  return (
    <textarea
      data-testid="textarea"
      value={text}
      onChange={handleChange}
    />
  )
}

export default AutocorrectTextarea;