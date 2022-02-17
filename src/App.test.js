import { render, screen, fireEvent } from '@testing-library/react';
import App from './App';


test('artist is added to list', () => {
  render(<App />);
  const addArtist = screen.getByText("Add artist");
  expect(addArtist).not.toBeNull();

  const addInput = screen.getByTestId("Add-Button");
  fireEvent.change(addInput, { target: { value: "artist-add-name" } });
  fireEvent.click(addArtist);

  const newArtist = screen.getByText("artist-add-name");
  expect(newArtist).toBeInTheDocument();
});


test('artist added text appears', () => {
  render(<App />);
  const addArtist = screen.queryByText("Add artist");
  expect(addArtist).toBeInTheDocument();

  const addInput = screen.getByTestId("Add-Button");
  fireEvent.change(addInput, { target: { value: "artist-add-name" } });
  fireEvent.click(addArtist);

  expect(screen.getByText('Artist added!')).toBeInTheDocument();
});


test('artist saved text appears', () => {
  render(<App />);
  const saveArtist = screen.getByText("Save");
  expect(saveArtist).not.toBeNull();

  const saveInput = screen.getByTestId("Save-Button");
  fireEvent.change(saveInput, { target: { value: "artist-saved-list" } });
  fireEvent.click(saveArtist);

  expect(screen.getByText('Saved artists list updated!')).toBeInTheDocument();
});
