
import { useState, useEffect } from 'react';
import axios, { AxiosResponse, AxiosError } from 'axios';

interface UseAxiosProps<T> {
  url: string;
  data?: T;
}

interface UseAxiosState<T> {
  data: T | null;
  error: AxiosError<T> | null;
  isLoading: boolean;
}





export const DefaultRequest = <T>({ url }: UseAxiosProps<T>): UseAxiosState<T> => {
  const [data, setData] = useState<T | null>(null);
  const [error, setError] = useState<AxiosError<T> | null>(null);
  const [isLoading, setIsLoading] = useState<boolean>(true);

  const fetchData = async (): Promise<void> => {
    setIsLoading(true);
    try {
      const response: AxiosResponse<T> = await axios.get(url);
      setData(response.data);
      setIsLoading(false);
    } catch (error: unknown) {
      setError(error as AxiosError<T>);
      setIsLoading(false);
    }
  };

  useEffect(() => {
    fetchData();
  // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [url]);


  useEffect(() => {
    setIsLoading(true);
  }, [url]);

  return { data, error, isLoading };
};

