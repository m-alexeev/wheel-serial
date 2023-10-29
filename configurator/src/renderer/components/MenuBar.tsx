import { FC } from 'react';
import { cn } from './utils';

interface MenuBarInterface {
  className?: string;
}

const MenuBar: FC<MenuBarInterface> = ({ className }) => {
  return (
    <div className={cn('flex bg-neutral justify-between p-2', className)}>
      {/* Controls */}
      <div className="flex">
        <button className="btn btn-sm btn-primary">Open</button>
      </div>
      <div className='flex gap-1'>
        <button className="btn btn-sm btn-secondary">Save</button>
        <button className="btn btn-sm btn-accent">Save As</button>
      </div>
    </div>
  );
};

export default MenuBar;
