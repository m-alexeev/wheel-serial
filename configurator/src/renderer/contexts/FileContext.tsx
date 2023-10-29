import { FC, ReactNode, createContext, useEffect, useState } from "react";

const DEFAULT_FILE = 'mapping.json'

interface FileContextInterface { 
  file: string | undefined;
  isLoadingFile: boolean;
  updateFile: (file: string | undefined) => void;
}

const FileContext = createContext<FileContextInterface| null>(null);

interface FileProps {
  children: ReactNode;
}

const FileContextProvider: FC<FileProps> = ({children}) => {
  const [file, setFile] = useState<string | undefined>(undefined);
  const [isLoadingFile, setLoadingFile] = useState(true);

  // Fetch last saved filename from localstorage
  useEffect(() => {
    // If localstorage is empty load default config json file
    // If custom config file does not exist, fall back to default config
    // If default config does not exist, re-create it
    // Default config path C:\Users\USERNAME\Documents\WheelDriver\mapping.json
  }, []);

  const updateFile = (fileName: string | undefined) => {
    setFile(fileName);

  }

  return(
    <FileContext.Provider value={{file, isLoadingFile, updateFile}}>
      {children}
    </FileContext.Provider>
  )
}