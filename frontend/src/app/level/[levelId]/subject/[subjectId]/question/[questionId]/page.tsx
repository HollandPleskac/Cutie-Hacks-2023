'use client'
import 'preline';

import useSWR from 'swr'
import { useRouter } from 'next/navigation'

export default function QuestionPage({ params }: any) {
    const router = useRouter()

    const { levelId, subjectId, questionId } = params;

    const fetcher = async (url: any) => {
        // console.log("fetching from url", url)
        const res = await fetch(url)
        if (!res.ok) {
            throw new Error(res.statusText);
        }
        // console.log("q/a pair result",resJSON ) // can only read res.json() once so make variable for it if need to log it here
        return res.json()
    }

    const apiUrl = levelId && subjectId && questionId ? `http://localhost:8000/${levelId}/${subjectId}/${questionId}` : null;

    const { data, error } = useSWR(apiUrl, fetcher);

    if (error) {
        console.log("see err", error)
        return (
            <div className='h-screen w-full bg-blue-400 flex justify-center items-center'>
                <p className='text-white text-lg'>Sorry, that question does not exist</p>
            </div>
        );
    }

    if (!data) return <div></div>;

    return (
        <div>
            {/* Topbar */}
            <header className="flex flex-wrap sm:justify-start sm:flex-nowrap z-50 w-full bg-white text-sm py-4 dark:bg-gray-800">
                <nav className="max-w-[85rem] w-full mx-auto px-4 sm:flex sm:items-center sm:justify-between" aria-label="Global">
                    <div className="flex items-center justify-between">
                        <a className="flex-none text-xl font-semibold dark:text-white" href="#">Brand</a>
                        <div className="sm:hidden">
                            <button type="button" className="hs-collapse-toggle p-2 inline-flex justify-center items-center gap-x-2 rounded-lg border border-gray-200 bg-white text-gray-800 shadow-sm hover:bg-gray-50 disabled:opacity-50 disabled:pointer-events-none dark:bg-transparent dark:border-gray-700 dark:text-white dark:hover:bg-white/10 dark:focus:outline-none dark:focus:ring-1 dark:focus:ring-gray-600" data-hs-collapse="#navbar-alignment" aria-controls="navbar-alignment" aria-label="Toggle navigation">
                                <svg className="hs-collapse-open:hidden flex-shrink-0 w-4 h-4" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="3" x2="21" y1="6" y2="6" /><line x1="3" x2="21" y1="12" y2="12" /><line x1="3" x2="21" y1="18" y2="18" /></svg>
                                <svg className="hs-collapse-open:block hidden flex-shrink-0 w-4 h-4" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 6 6 18" /><path d="m6 6 12 12" /></svg>
                            </button>
                        </div>
                    </div>
                    <div id="navbar-alignment" className="hs-collapse hidden overflow-hidden transition-all duration-300 basis-full grow sm:block">
                        <div className="flex flex-col gap-5 mt-5 sm:flex-row sm:items-center sm:mt-0 sm:ps-5">
                            <a className="font-medium text-blue-500 dark:focus:outline-none dark:focus:ring-1 dark:focus:ring-gray-600" href="#" aria-current="page">Landing</a>
                            <a className="font-medium text-gray-600 hover:text-gray-400 dark:text-gray-400 dark:hover:text-gray-500 dark:focus:outline-none dark:focus:ring-1 dark:focus:ring-gray-600" href="#">Account</a>
                            <a className="font-medium text-gray-600 hover:text-gray-400 dark:text-gray-400 dark:hover:text-gray-500 dark:focus:outline-none dark:focus:ring-1 dark:focus:ring-gray-600" href="#">Work</a>
                            <a className="font-medium text-gray-600 hover:text-gray-400 dark:text-gray-400 dark:hover:text-gray-500 dark:focus:outline-none dark:focus:ring-1 dark:focus:ring-gray-600" href="#">Blog</a>
                        </div>
                    </div>
                </nav>
            </header>

            <div className=' h-screen w-full flex flex-col justify-center items-center' style={{ height: 'calc(100vh - 60px)' }} >
                {data.question + 'what is 5x5'}
                <h1 className='' >{data.answer + '25'}</h1>
                <input type="text" className='my-9 ring-2 ring-blue-500'></input>
                <button className=' px-8 py-3 rounded-lg my-8 bg-blue-500 ring-1 ring-slate-500 ring-offset-1 ring-offset-slate-50 dark:ring-offset-slate-900' onClick={() => {
                    if (router)
                        router.push(`/level/${levelId}/subject/${subjectId}/question/${parseInt(questionId) + 1}`)
                }} >Next</button>
            </div>

        </div>

    );
}