import { ChangeEvent, FC, ReactNode } from 'react';

export type selectOptionType = {
  value: string;
  text: string;
};

interface DropdownInterface {
  options: selectOptionType[];
  onSelect: (index: number, text: string) => void;
}

const Dropdown: FC<DropdownInterface> = ({ options, onSelect }) => {
  const selectElement = (element: ChangeEvent<HTMLSelectElement>) => {
    onSelect(element.target.selectedIndex, element.target.value);
  };

  return (
    <select
      className="select select-bordered w-full max-w-xs"
      onChange={selectElement}
    >
      {options.map((option, index) => {
        return <option key={index} value={option.value}>{option.text}</option>;
      })}
    </select>
  );
};

export default Dropdown;
