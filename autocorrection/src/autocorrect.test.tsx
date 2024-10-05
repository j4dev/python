import React from 'react';
import { describe, it, expect } from 'vitest';
import { render, fireEvent } from '@testing-library/react';
import AutocorrectTextarea from './autocorrect';

describe('AutocorrectTextarea', () => {
  it('renders correctly', () => {
    const { getByTestId } = render(<AutocorrectTextarea corrections={{}} />);
    
    const textarea = getByTestId('textarea') as HTMLTextAreaElement;
    expect(textarea).toBeTruthy();
  });

  it('should autocorrect words based on corrections prop', () => {
    const corrections = {
      'realy': 'really',
      'wierd': 'weird',
    };

    const { getByTestId } = render(<AutocorrectTextarea corrections={corrections} />);
    const textarea = getByTestId('textarea') as HTMLTextAreaElement;

    fireEvent.change(textarea, { target: { value: 'This is realy ' } });

    expect(textarea.value).toBe('This is really ');
  });

  it('does not autocorrect words not in corrections prop', () => {
    const corrections = {
      'realy': 'really',
    };

    const { getByTestId } = render(<AutocorrectTextarea corrections={corrections} />);
    const textarea = getByTestId('textarea') as HTMLTextAreaElement;

    fireEvent.change(textarea, { target: { value: 'This is cool ' } });

    expect(textarea.value).toBe('This is cool ');
  });
});