import { ChangeEvent, FC, useState } from 'react';
import MenuBar from '../components/MenuBar';

const Home: FC = () => {
  const [selectedFile, setSelectedFile] = useState<File | null>(null);

  const handleFileChange = (e: ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files && e.target.files[0];
    if (file) {
      setSelectedFile(file);
    }
  };


  return (
    <div className='flex flex-col h-screen'>
      <div className='grow bg-slate-700'>Main Screen</div>
      <MenuBar className='grow-0'/>
    </div>
  );
};

export default Home;
